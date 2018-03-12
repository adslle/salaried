from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect
from user.forms import UserForm


# Create your views here.

# user list
@login_required
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    # check if get request has keyword param
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        items = User.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))  # like %keyword%
    else:
        items = User.objects.all()
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
    return render(request, 'user/index.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def show(request, id):
    item = User.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'user/show.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data["password"]
        user.set_password(password)
        user.save()
        messages.info(request, 'user created')
        return redirect('user.index')

    context = {
        'form': form
    }
    return render(request, 'user/form.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def update(request, id):
    item = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=item)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data["password"]
        user.set_password(password);
        user.save();
        messages.info(request, 'user updated')

        return redirect('user.index')

    context = {
        'form': form
    }
    return render(request, 'user/form.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete(request, id):
    item = User.objects.get(id=id)
    print(item)
    print(item.id)
    print(id)
    if request.method == 'POST':
        if not item.is_staff:
            item.delete()
            messages.info(request, 'user removed')
        else:
            messages.info(request, 'you can\'t remove you')
        return redirect('user.index')
    return redirect('user.index')
