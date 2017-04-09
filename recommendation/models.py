from django.db import models
from django.urls import reverse

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return str(self.name)


class Keyword(models.Model):
    keyword_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return '{}'.format(self.name)


class MovieCast(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
        blank=True, null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE,
        blank=True, null=True)
    movie_character = models.CharField(max_length=300, blank=True, null=True)
    cast_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return '{}, {}, {}'.format(self.movie, self.person,
            self.movie_character)


class MovieCrew(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
        blank=True, null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE,
        blank=True, null=True)
    department = models.CharField(max_length=25, blank=True, null=True)
    job = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return '{}, {}, {}'.format(self.movie, self.person, self.job)


class MovieGenre(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
        blank=True, null=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE,
        blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return str(self.genre)


class MovieKeyword(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,
        blank=True, null=True)
    keyword = models.ForeignKey('Keyword', on_delete=models.CASCADE,
        blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return '{}, {}'.format(self.movie, self.keyword)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    imdb_id = models.CharField(max_length=9, blank=True, null=True)
    poster_path = models.CharField(max_length=32, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    vote_average = models.DecimalField(max_digits=3,
        decimal_places=1, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    popularity = models.DecimalField(max_digits=10,
        decimal_places=6, blank=True, null=True)
    budget = models.IntegerField(blank=True, null=True)
    revenue = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)

    # custom connecitons fields
    genres = models.ManyToManyField('Genre', through='MovieGenre')
    keywords = models.ManyToManyField('Keyword', through='MovieKeyword')

    #cast = self.object.MovieCast.all()
    #cast = models.ManyToManyField('Person', through='MovieCast')
    #crew = models.ManyToManyField('Person', through='MovieCrew')



    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return '{}'.format(self.title)


class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    deathday = models.DateField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=150, blank=True, null=True)
    popularity = models.DecimalField(max_digits=11,
        decimal_places=6, blank=True, null=True)
    profile_path = models.CharField(max_length=34, blank=True, null=True)

    class Meta:
        managed = True

    def __str__(self):
        # returns string representation of the model object
        return '{}'.format(self.name)
