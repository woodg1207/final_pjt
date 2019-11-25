from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
@login_required
def index(request):
    user_prefers = request.user.genre_prefers.all()
    movies = Movie.objects.order_by('-vote_average')
    selected_movies = []
    if user_prefers:
        for genre in user_prefers:
            genres = Genre.objects.filter(pk=genre.pk)
            selected_movies += genres[0].movies.all()
    context = {'movies': movies, 'selected_movies': selected_movies,}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    reviewform = ReviewForm()
    context = {'movie':movie, 'reviewform':reviewform, 'reviews': reviews}
    return render(request, 'movies/detail.html', context)

@require_POST
def review_create(request, movie_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie_id=movie_pk
                review.user = request.user
                review.save()
                return redirect('movies:detail', movie_pk)
    return redirect('movies:detail', movie_pk)


@login_required
def select_genre(request):
    if request.user.genre_prefers:
        return redirect('movies:index')
    if request.method == 'POST':
        return redirect('movies:index')
    else:
        genres = Genre.objects.all()
        context = {'genres': genres,}
        return render(request, 'movies/select_genre', context)
