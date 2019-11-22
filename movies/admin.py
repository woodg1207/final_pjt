from django.contrib import admin
from .models import Genre, Movie, Review

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content', )