# constellations/views.py

from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.utils import timezone
from .models import Constellation
from .forms import ConstellationForm

from braces.views import LoginRequiredMixin

# Create your views here.
class ConstellationListView(generic.ListView):
    model = Constellation
    template_name = 'constellations/constellation_list.html'
    ordering = ['constellation_name']
    context_object_name = 'constellation'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ConstellationListView, self).get_context_data(**kwargs)
        context['constellation_count'] = Constellation.objects.count()
        context['nav_Constellation'] = True
        return context


class ConstellationDetailView(generic.DetailView):
    model = Constellation
    template_name = 'constellations/constellation_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConstellationDetailView, self).get_context_data(**kwargs)
        context['nav_constellation'] = True
        return context


class ConstellationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Constellation
    form_class = ConstellationForm

    def get_success_url(self):
        return reverse_lazy('constellation:constellation-detail', args= (self.object.id,))


class ConstellationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Constellation
    form_class = ConstellationForm
    success_url = '/constellations/'
    template_name = 'constellations/constellation_form.html'

    def form_valid(self, form):
        return super(ConstellationCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(ConstellationCreateView, self).form_invalid(form)


class ConstellationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Constellation
    success_url = reverse_lazy('constellation:constellation-list')
