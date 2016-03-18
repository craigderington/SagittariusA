# galaxies/urls.py
from django.conf.urls import url, include
from . import views

urlpatterns = [
url(
    regex=r'^$',
    view=views.GalaxyListView.as_view(),
    name='galaxy-list'
),
url(
    regex=r'^add/',
    view=views.GalaxyCreateView.as_view(),
    name='galaxy-add'
),
url(
    regex=r'^(?P<pk>[0-9]+)/$',
    view=views.GalaxyDetailView.as_view(),
    name='galaxy-detail'
),
url(
    regex=r'^(?P<pk>[0-9]+)/update/$',
    view=views.GalaxyUpdateView.as_view(),
    name='galaxy-update'
),
url(
    regex=r'^(?P<pk>[0-9]+)/delete/$',
    view=views.GalaxyDeleteView.as_view(),
    name='galaxy-delete'
),
]
