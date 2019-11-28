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
    like_genre_movies = []
    if request.user.like_movies.all():
        check= []
        for movie in request.user.like_movies.all():
            for genre in movie.genres.all():
                if genre.name in check: continue
                check.append(genre.name)
                like_genre = Genre.objects.filter(pk=genre.pk)
                like_genre_movies += like_genre[0].movies.all()
    selected_movies = []
    if user_prefers:
        for genre in user_prefers:
            user_genre = Genre.objects.filter(pk=genre.pk)
            selected_movies += user_genre[0].movies.all()
    context = {'movies': movies, 'selected_movies': selected_movies, 'like_genre_movies':like_genre_movies}
    return render(request, 'movies/index.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set.all()
    sum_value = 0.0
    if len(reviews):
        for review in reviews:
            sum_value += review.score
        average_value = sum_value / len(reviews)
    else:
        average_value = 0.0
    reviewform = ReviewForm()
    context = {'movie':movie, 'reviewform':reviewform, 'reviews': reviews, 'average_value': round(average_value, 2),}
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
    # select genres
    user_prefers = request.user.genre_prefers.all()
    if request.method == 'POST':
        if len(user_prefers.all()):
            for pre_value in user_prefers:
                genre = get_object_or_404(Genre, pk=pre_value.pk)
                genre.user_prefers.remove(request.user)
            genres = Genre.objects.all()
            context = {'genres': genres,}
            return render(request, 'movies/select_genre.html', context)  
        check_var = request.POST.getlist('checks')
        if check_var:
            for value in check_var:
                value = int(value)
                genre = get_object_or_404(Genre, pk=value)
                genre.user_prefers.add(request.user)
        return redirect('movies:index')
    else:
        if user_prefers:
            return redirect('movies:index')
        genres = Genre.objects.all()
        context = {'genres': genres,}
        return render(request, 'movies/select_genre.html', context)

@login_required
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:detail', movie_pk)

@login_required
def all(request):
    movies = Movie.objects.order_by('-vote_average')
    context = {'movies':movies, }
    return render(request, 'movies/all.html', context)


def follow(request, movie_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
    return redirect('movies:detail', movie_pk)


@require_POST
def review_delete(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('movies:detail', movie_pk)


def review_update(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('movies:detail', movie_pk)
    context = {'form': form, 'score':review.score,}
    return render(request, 'movies/review_update.html', context)