import json
from pprint import pprint


with open('now_playing.json','r', encoding='UTF8') as f:
    jdata = json.load(f)

with open('genre.json', 'r', encoding='UTF8') as g:
    gdata = json.load(g)

movies = []
for idx, data in enumerate(jdata.get("results")):
    movie = {}
    fields = {}
    movie["pk"] = idx+1
    movie["model"] = "movies.Movie"
    fields["title"] = data.get("title")
    fields["poster_path"] = data.get("poster_path")
    fields["backdrop_path"] = data.get("backdrop_path")
    fields["overview"] = data.get("overview")
    fields["vote_average"] = data.get("vote_average")
    fields["popularity"] = data.get("popularity")
    fields["original_title"] = data.get("original_title")
    genres = []
    for i in range(len(data.get('genre_ids'))):
       genres.append(data['genre_ids'][i]) 
    fields["genres"] = genres
    movie["fields"] = fields
    movies.append(movie)

with open('now_movie.json', 'w', encoding='utf-8') as make:
    json.dump(movies, make, indent='\t')

genres = []
for idx, data in enumerate(gdata.get('genres')):
    genre = {}
    genre['pk'] = data.get('id')
    genre['model'] = 'movies.genre'
    genre['feilds'] = data.get('name')
    genres.append(genre)

with open('now_genre.json', 'w', encoding='utf-8') as G:
    json.dump(genres, G, indent='\t')