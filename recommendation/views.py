from django.http import Http404
from django.shortcuts import render
from django.views import generic

from .models import *

# Home page
def home(request):

    return render(request, 'recommendation/home.html')

# Movie list page
class MovieListView(generic.ListView):
    model = Movie
    template_name = 'recommendation/movie_list.html'
    paginate_by = 10

    @property
    def filtered_genres(self):
        if not hasattr(self, '_filtered_genres'):
            checked_genres = self.request.GET.getlist('genre')
            self._filtered_genres = Genre.objects.filter(
                pk__in=checked_genres or [])
        return self._filtered_genres


    def get_queryset(self):
        query = super(MovieListView, self).get_queryset()
        #if self.filtered_years:
            #years = self.filtered_years
            #print (years)
        if self.filtered_genres:
            genres = self.filtered_genres
            for genre in genres:
                query = query.filter(genres=genre)

        return query.order_by('-vote_count')

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['filtered_genres'] = self.filtered_genres
        #years = Movie.objects.all().dates('release_date', 'year')
        #context['years_list'] = years

        # query_url for pagination without ('page=N')
        query_url = self.request.GET.urlencode()
        splited = query_url.split('&')
        if splited[0][0:4] == 'page':
            query_url = '&'.join(splited[1:])
        context['query_url'] = query_url

        return context

# Movie detail page
class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'recommendation/movie_detail.html'

# Person list page
class PersonListView(generic.ListView):
    model = Person
    template_name = 'recommendation/person_list.html'
    paginate_by = 10

    def get_queryset(self):

        return Person.objects.order_by('-popularity')

# Person detail page
class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'recommendation/person_detail.html'
