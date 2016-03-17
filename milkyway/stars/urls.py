# stars/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.StarListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^star/(?P<pk>\d+)/$',
        view=views.StarDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^star/(?P<pk>\d+)/update/$',
        view=views.StarUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^star/add/$',
        view=views.StarCreateView.as_view(),
        name='star-add'
    ),
    url(
        regex=r'^star/(?P<pk>[0-9]+)/delete/$',
        view=views.StarDeleteView.as_view(),
        name='star-delete'
    ),
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
    )
]
