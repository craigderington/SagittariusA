#galaxies/views.py

from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.utils import timezone
from galaxies.models import Galaxy
from .forms import GalaxyForm

# Create your views here.

class GalaxyListView(generic.ListView):
    model = Galaxy
    template_name = 'stars/galaxy_list.html'

    def get_context_data(self, **kwargs):
        context = super(GalaxyListView, self).get_context_data(**kwargs)
        context['galaxy_count'] = Galaxy.objects.count()
        context['nav_galaxy'] = True
        return context


class GalaxyDetailView(generic.DetailView):
    model = Galaxy
    template_name = 'stars/galaxy_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GalaxyDetailView, self).get_context_data(**kwargs)
        context['nav_galaxy'] = True
        return context


class GalaxyCreateView(generic.CreateView):
    model = Galaxy
    form_class = GalaxyForm
    success_url = 'stars/galaxies/'
    template_name = 'stars/galaxy_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(GalaxyCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(GalaxyCreateView, self).form_invalid(form)


class GalaxyUpdateView(generic.UpdateView):
    model = Galaxy
    form_class = GalaxyForm

    def get_success_url(self):
        return reverse_lazy('stars:galaxy-detail', args= (self.object.id,))


class GalaxyDeleteView(generic.DeleteView):
    model = Galaxy
    success_url = reverse_lazy('stars:galaxy-list')
