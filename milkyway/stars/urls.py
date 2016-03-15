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
        regex=r'^(?P<pk>\d+)/$',
        view=views.StarDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.StarUpdateView.as_view(),
        name='update'
    ),
]
