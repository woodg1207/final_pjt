from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies,}
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

# @login_required
# def review_delete(request, movie)