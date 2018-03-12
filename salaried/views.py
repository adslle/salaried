from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse

from salaried.forms import SalariedForm, DocumentForm
from salaried.models import Salaried, Document


# Create your views here.

# salaried list
@login_required
def index(request):
    # check if get request has keyword param
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        items = Salaried.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
    else:
        items = Salaried.objects.all()
        keyword = ""

    paginator = Paginator(items, 10)  # Show 25 contacts per page
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
    return render(request, 'salaried/index.html', context)


@login_required
def show(request, id):
    item = Salaried.objects.get(id=id)
    documents = item.document_set.all();
    context = {
        'item': item,
        'documents': documents
    }
    return render(request, 'salaried/show.html', context)


@login_required
def create(request):
    document_formset_factory = formset_factory(DocumentForm)
    form = SalariedForm()
    data = {
        # 'form-TOTAL_FORMS': '2',
        # 'form-INITIAL_FORMS': '0',
        # 'form-MAX_NUM_FORMS': '',
        # 'form-0-label': 'CIN',
        # 'form-0-description': '',
        # 'form-1-label': 'CV',
        # 'form-1-description': '',
    }
    if request.method == 'GET':
        context = {
            'form': form,
            'document_form_set': document_formset_factory
        }
        return render(request, 'salaried/form.html', context)

    if request.method == 'POST':
        form = SalariedForm(request.POST)
        document_formset = document_formset_factory(request.POST, request.FILES)
        if form.is_valid() and document_formset.is_valid():
            s = form.save()
            for doc in document_formset:
                fd = doc.save(commit=False)
                fd.salaried = s
                fd.save()
            messages.info(request, 'new salaried created')
            return redirect('salaried.index')
        else:
            context = {
                'form': form,
                'document_form_set': document_formset
            }
            return render(request, 'salaried/form.html', context)


@login_required
def update(request, id):
    item = Salaried.objects.get(id=id)
    form = SalariedForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.info(request, 'salaried updated')
        return redirect('salaried.index')

    context = {
        'form': form
    }
    return render(request, 'salaried/form-update.html', context)


@login_required
def delete(request, id):
    item = Salaried.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        messages.info(request, 'salaried removed')
        return redirect('salaried.index')
    return redirect('salaried.index')


@login_required
def delete_document(request, salaried_id, document_id):
    item = Salaried.objects.get(id=salaried_id)
    document = item.document_set.get(id=document_id);
    if request.method == 'POST':
        document.delete()
        messages.info(request, 'document removed')
        return redirect('salaried.show', salaried_id)
    return redirect('salaried.show', salaried_id)


@login_required
def create_document(request, salaried_id):
    item = Salaried.objects.get(id=salaried_id)
    form = DocumentForm(request.POST or None, request.FILES or None)
    print(form)
    if form.is_valid():
        fd = form.save(commit=False)
        fd.salaried = item
        fd.save()
        messages.info(request, 'document created')
        return redirect('salaried.show', item.id)
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'salaried/document-form.html', context)


@login_required
def update_document(request, salaried_id, document_id):
    item = Salaried.objects.get(id=salaried_id)
    document_item = item.document_set.get(id=document_id)
    form = DocumentForm(request.POST or None, instance=document_item)
    if form.is_valid():
        fd = form.save(commit=False)
        fd.salaried = item
        fd.save()
        messages.info(request, 'document updated')
        return redirect('salaried.show', item.id)
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'salaried/document-form.html', context)
