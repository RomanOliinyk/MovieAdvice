from django.conf.urls import url

from . import views

app_name = 'recommendation'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^movie/$', views.MovieListView.as_view(), name = 'movie'),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieDetailView.as_view(),
        name='movie-detail'),
    #url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
]
