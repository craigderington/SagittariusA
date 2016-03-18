# stars/views.py

from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.utils import timezone
from .models import Star
from .forms import StarForm

from braces.views import LoginRequiredMixin

# Create your views here.
class StarListView(generic.ListView):
    model = Star
    template_name = 'stars/star_list.html'
    ordering = ['proper_name']
    context_object_name = 'star'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(StarListView, self).get_context_data(**kwargs)
        context['star_count'] = Star.objects.count()
        context['nav_star'] = True
        return context


class StarDetailView(generic.DetailView):
    model = Star
    template_name = 'stars/star_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StarDetailView, self).get_context_data(**kwargs)
        context['nav_star'] = True
        return context


class StarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Star
    form_class = StarForm

    def get_success_url(self):
        return reverse_lazy('stars:detail', args= (self.object.id,))


class StarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Star
    form_class = StarForm
    success_url = '/stars/'
    template_name = 'stars/star_form.html'

    def form_valid(self, form):
        return super(StarCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(StarCreateView, self).form_invalid(form)


class StarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Star
    success_url = reverse_lazy('stars:star-list')
