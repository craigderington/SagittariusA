# stellar_objects/views.py

from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.utils import timezone
from .models import StellarObject
from .forms import StellarObjectForm

from braces.views import LoginRequiredMixin

# Create your views here.
class StellarObjectListView(generic.ListView):
    model = StellarObject
    template_name = 'stellar_objects/stellar_objects_list.html'
    ordering = ['name']
    context_object_name = 'stellar'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(StellarObjectListView, self).get_context_data(**kwargs)
        context['stellar_count'] = StellarObject.objects.count()
        context['nav_stellar'] = True
        return context


class StellarObjectDetailView(generic.DetailView):
    model = StellarObject
    template_name = 'stellar_objects/stellar_objects_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StellarObjectDetailView, self).get_context_data(**kwargs)
        context['nav_stellar'] = True
        return context


class StellarObjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = StellarObject
    form_class = StellarObjectForm

    def get_success_url(self):
        return reverse_lazy('stellar:stellar-detail', args= (self.object.id,))


class StellarObjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = StellarObject
    form_class = StellarObjectForm
    success_url = '/stellar_objects/'
    template_name = 'stellar_objects/stellar_objects_form.html'

    def form_valid(self, form):
        return super(StellarObjectCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(StellarObjectCreateView, self).form_invalid(form)


class StellarObjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = StellarObject
    success_url = reverse_lazy('stellar:stellar-list')
