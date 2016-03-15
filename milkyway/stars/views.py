# stars/views.py
from django.views import generic
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from stars.models import Star

# Create your views here.

class StarListView(generic.ListView):
    model = Star
    template_name = 'stars/star_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(StarListView, self).get_context_data(**kwargs)
        return context


class StarDetailView(generic.DetailView):
    model = Star
    template_name = 'stars/star_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StarDetailView, self).get_context_data(**kwargs)
        return context


class StarUpdateView(generic.UpdateView):
    model = Star

    def get_success_url(self):
        return reverse('stars:detail',
                       kwargs={'pk', self.object.pk})
