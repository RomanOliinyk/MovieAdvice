import operator
from functools import reduce

from django.http import Http404
from django.shortcuts import render
from django.views import generic
from django.db.models import Q

# Postgres Search module
#from django.contrib.postgres.search import SearchVector

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
        if not hasattr(self, '_filtered_genre'):
            checked_genres = self.request.GET.getlist('genre')
            self._filtered_genres = Genre.objects.filter(
                pk__in=checked_genres or [])
        return self._filtered_genres

    @property
    def filtered_years(self):
        if not hasattr(self, '_filtered_years'):
            checked_years = self.request.GET.get('year')
        return checked_years


    def get_queryset(self):
        query = super(MovieListView, self).get_queryset()
        if self.filtered_years:
            years = self.filtered_years
            if years != 'any':
                query = query.filter(release_date__year = years)
        if self.filtered_genres:
            genres = self.filtered_genres
            for genre in genres:
                query = query.filter(genres=genre)

        # trying out search
        query_search = self.request.GET.get('q')
        if query_search:
            query_list = query_search.split()
            query = query.filter(
                reduce(operator.and_,
                    (Q(title__search=q) for q in query_list)))


        return query.order_by('-vote_count')

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        context['filtered_genres'] = self.filtered_genres
        years = Movie.objects.all().dates('release_date', 'year')
        context['years'] = years

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

    def simular_movies_genre(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        genre_list = []
        for item in context['movie'].genres.all():
            genre_list.append(item.genre_id)
        movie_query = Movie.objects.all()
        genre_query = []
        genre_recommendation = []

        if genre_list:
            while len(genre_list) > 0:
                modified_query = movie_query
                for genre in genre_list:
                    modified_query = modified_query.filter(genres=genre)
                genre_list.pop()
                genre_query.append(modified_query)

        movie_id = context['movie'].movie_id
        movie_vote = context['movie'].vote_average
        movie_pop = context['movie'].popularity

        for group in genre_query:
            for item in group:
                if len(genre_recommendation) >= 5:
                    break
                if (item.movie_id != movie_id) and (
                    item not in genre_recommendation) and (
                    movie_vote -2 <= item.vote_average <= movie_vote +2):
                    genre_recommendation.append(item)

        return genre_recommendation

    def simular_movies_keyword(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        keyword_list = []

        for item in context['movie'].keywords.all():
            keyword_list.append(item.keyword_id)
        movie_id = context['movie'].movie_id
        movie_query = Movie.objects.all().exclude(movie_id=movie_id)

        while len(keyword_list) >= 1:
            if len(movie_query) < 20:
                break
            keyword_query = []
            top_keyword = None
            empty_keyword_list = []

            for item in keyword_list:
                temp_query = movie_query.filter(keywords=item)
                if len(temp_query) == 0:
                    empty_keyword_list.append(item)
                elif len(temp_query) > len(keyword_query):
                    keyword_query = temp_query
                    top_keyword = item

            if top_keyword is not None:
                keyword_list.remove(top_keyword)
            if len(empty_keyword_list) > 0:
                keyword_list = list(set(keyword_list)-set(empty_keyword_list))

            movie_query = keyword_query

        if len(keyword_query) > 35:
            keyword_query = None
        if keyword_query is not None:
            return keyword_query



    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['genre_query'] = self.simular_movies_genre()
        context['keyword_query'] = self.simular_movies_keyword()
        context['cast_list'] = list(
            reversed(context['movie'].moviecast_set.all()))
        context['cast_length'] = len(context['cast_list'])
        context['crew_list'] = list(
            reversed(context['movie'].moviecrew_set.exclude(
            job='Director')))
        context['crew_length'] = len(context['crew_list'])
        context['director'] = context['movie'].moviecrew_set.filter(
            job='Director')

        return context

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
