from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView, UpdateView, DeleteView, CreateView
from .models import Reference
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your views here.

class ReferenceListView(LoginRequiredMixin, ListView):
    queryset = Reference.referenceList.all()
    contextName = 'references'
    templateName = 'reference/reference_list.html'
    
    def get_queryset(self):
        
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        
        return super().get_context_data(**kwargs)

class ReferenceDetailView(LoginRequiredMixin, FormView):
    model = Reference
    template_name = 'reference/reference_detail.html'
    
    def get_initial(self):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        self.reference = get_object_or_404(Reference, pk = pk, slug = slug)
        
        return super().get_initial()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reference'] = self.reference
        
        return context
    
class ReferenceCreateView(CreateView):
    model = Reference
    fields = ['title', 'description', 'link', 'author']
    templateName = 'reference/reference_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title, allow_unicode = True)
        return super().form_valid(form)
    
class ReferenceUpdateView(UpdateView):
    model = Reference
    fields = ['title', 'description', 'link', 'author']
    templateName = 'reference/reference_form.html'
    queryPK = True
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        return qs.filter(author = self.request.user)
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title, allow_unicode=True)
        
        return super().form_valid(form)
    
class ReferenceDeleteView(DeleteView):
    model = Reference
    templateName = 'reference/reference_confirm_delete.html'
    successURL = reverse_lazy('reference:reference_list')
    queryPK = True
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        return qs.filter(author = self.request.user)
    
        