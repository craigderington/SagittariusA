# galaxies/urls.py
from django.conf.urls import url, include
from . import views

urlpatterns = [
url(
    regex=r'^$',
    view=views.ConstellationListView.as_view(),
    name='constellation-list'
),
url(
    regex=r'^add/',
    view=views.ConstellationCreateView.as_view(),
    name='constellation-add'
),
url(
    regex=r'^(?P<pk>[0-9]+)/$',
    view=views.ConstellationDetailView.as_view(),
    name='constellation-detail'
),
url(
    regex=r'^(?P<pk>[0-9]+)/update/$',
    view=views.ConstellationUpdateView.as_view(),
    name='constellation-update'
),
url(
    regex=r'^(?P<pk>[0-9]+)/delete/$',
    view=views.ConstellationDeleteView.as_view(),
    name='constellation-delete'
),
]
