# galaxies/urls.py
from django.conf.urls import url, include

urlpatterns = [
url(
    regex=r'^galaxies/$',
    view=views.GalaxyListView.as_view(),
    name='galaxy-list'
),
url(
    regex=r'^galaxy/add/',
    view=views.GalaxyCreateView.as_view(),
    name='galaxy-add'
),
url(
    regex=r'^galaxy/(?P<pk>[0-9]+)/$',
    view=views.GalaxyDetailView.as_view(),
    name='galaxy-detail'
),
url(
    regex=r'^galaxy/(?P<pk>[0-9]+)/update/$',
    view=views.GalaxyUpdateView.as_view(),
    name='galaxy-update'
),
url(
    regex=r'^galaxy/(?P<pk>[0-9]+)/delete/$',
    view=views.GalaxyDeleteView.as_view(),
    name='galaxy-delete'
),
]
