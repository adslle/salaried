from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from bu.forms import BUForm
from bu.models import BU


# Create your views here.

#bu list
@login_required
def index(request):
    #check if get request has keyword param
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        items = BU.objects.filter(name__contains=keyword) #like %keyword%
    else:
        items = BU.objects.all()
        keyword = ""

    paginator = Paginator(items, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    items_page = paginator.get_page(page)

    index = items_page.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    context = {
        'items': items_page,
        'keyword': keyword,
        'page_range': page_range,
    }
    # print vars(posts_chunked)
    return render(request, 'bu/index.html', context)


@login_required
def show(request, id):
    item = BU.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'bu/show.html', context)

@login_required
def create(request):
    form = BUForm(request.POST or None)
    if form.is_valid():
        form.save()

        messages.info(request, 'business unit created')
        return redirect('bu.index')

    context = {
        'form': form
    }
    return render(request, 'bu/form.html', context)


@login_required
def update(request,id):
    item = BU.objects.get(id=id)
    form = BUForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        messages.info(request, 'business unit updated')
        return redirect('bu.index')

    context = {
        'form': form
    }
    return render(request, 'bu/form.html', context)

@login_required
def delete(request,id):
    item = BU.objects.get(id=id)
    print(item)
    print(item.id)
    print(id)
    if request.method == 'POST':
        item.delete()
        messages.info(request, 'business unit deleted')
        return redirect('bu.index')

    messages.info(request, 'something wrong')
    return redirect('bu.index')

