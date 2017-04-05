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

    def get_queryset(self):
        return Movie.objects.order_by('-vote_count')

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'recommendation/movie_detail.html'

#def index(request):
    #movie_list = Movie.objects.order_by('-vote_count')[:10]
    #context = {
        #'movie_list': movie_list,
    #}
    #return render(request, 'recommendation/index.html', context)

#def detail(request, movie_id):
#    try:
#        movie = Movie.objects.get(pk=movie_id)
#        cast = Movie.moviecast_set
#    except Movie.DoesNotExist:
#        raise Http404('Movie does not exist!')
#    return render(request, 'recommendation/detail.html', {'movie': movie,
#        'cast': cast})
