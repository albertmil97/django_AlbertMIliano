from django.shortcuts import render, get_object_or_404
from .models import Reference
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def reference_list(request):
    object_list = Reference.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        references = paginator.page(page)
    except PageNotAnInteger:
        references = paginator.page(1)
    except EmptyPage:
        references = paginator.page(paginator.num_pages)
    return render(request,'reference/reference_list.html',
                            {'references':references,'page':page})
def reference_detail(request, year, month, day, reference):
    reference = get_object_or_404(Reference, slug=reference,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                'reference/reference_detail.html',
                {'reference' : reference,})

class ReferenceCreateView(CreateView):
    model = Reference
    fields = ['author','title', 'slug', 'description', 'link']

class ReferenceUpdateView(UpdateView):
    model = Reference
    fields = ['author','title', 'slug', 'description', 'link']

class ReferenceDeleteView(DeleteView):
    model = Reference
    success_url = reverse_lazy('reference:reference_list')