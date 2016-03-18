# stars/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.StarListView.as_view(),
        name='star-list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.StarDetailView.as_view(),
        name='star-detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.StarUpdateView.as_view(),
        name='star-update'
    ),
    url(
        regex=r'^add/$',
        view=views.StarCreateView.as_view(),
        name='star-add'
    ),
    url(
        regex=r'^(?P<pk>[0-9]+)/delete/$',
        view=views.StarDeleteView.as_view(),
        name='star-delete'
    ),
]
