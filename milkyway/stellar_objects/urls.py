# galaxies/urls.py
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.StellarObjectListView.as_view(),
        name='stellar-list'
    ),
    url(
        regex=r'^add/',
        view=views.StellarObjectCreateView.as_view(),
        name='stellar-add'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/$',
        view=views.StellarObjectDetailView.as_view(),
        name='stellar-detail'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/update/$',
        view=views.StellarObjectUpdateView.as_view(),
        name='stellar-update'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/delete/$',
        view=views.StellarObjectDeleteView.as_view(),
        name='stellar-delete'
    ),
]
