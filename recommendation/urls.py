from django.conf.urls import url

from . import views

app_name = 'recommendation'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^movie/$', views.MovieListView.as_view(), name='movie-list'),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetailView.as_view(),
        name='movie-detail'),
    url(r'^person/$', views.PersonListView.as_view(), name='person-list'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(),
        name='person-detail'),
]
