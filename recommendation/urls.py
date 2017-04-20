from django.conf.urls import url

from . import views

app_name = 'recommendation'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^movie/$', views.MovieListView.as_view(), name='movie_list'),
    url(r'^movie/(?P<pk>\d+)/', views.MovieDetailView.as_view(),
        name='movie_detail'),
    url(r'^people/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^person/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(),
        name='person_detail'),
]
