from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    user_prefers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='genre_prefers', blank=True)


class Actor(models.Model):
    name = models.CharField(max_length=40)
    profile_path = models.CharField(max_length=150)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors', blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=40)
    poster_path = models.CharField(max_length=150)
    backdrop_path = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    overview = models.TextField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    original_title = models.CharField(max_length=30)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)


class Review(models.Model):
    content = models.CharField(max_length=150)
    score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)