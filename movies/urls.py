from django.urls import path
from . import views


app_name='movies'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/reviews/', views.review_create, name='review_create'),
    path('', views.select_genre, name='select_genre'),
    path('<int:movie_pk>/likes/', views.like, name='like'),
    path('allmovies/', views.all, name='all'),
]
