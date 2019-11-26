import json
from pprint import pprint
from decouple import config
import requests
from copy import deepcopy

# key = config('API_KEY')
key = 'c9ce586a25f99f5a58ec0e50547b7b7c'
with open('movie.json','r', encoding='UTF8') as f:
    jdata = json.load(f)

with open('genre.json', 'r', encoding='UTF8') as g:
    gdata = json.load(g)

movies = []
actors = []

for idx, data in enumerate(jdata.get("results")):
    url = 'https://api.themoviedb.org/3/movie/'
    movie = {}
    actor = {}
    fields = {}
    fields_a = {}
    movie["pk"] = idx+1
    movie["model"] = "movies.Movie"
    fields["title"] = data.get("title")
    if data['poster_path']:
        fields["poster_path"] = data.get("poster_path")
    if data['backdrop_path']:
        fields["backdrop_path"] = data.get("backdrop_path")
    fields["overview"] = data.get("overview")
    fields["vote_average"] = data.get("vote_average")
    fields["popularity"] = data.get("popularity")
    fields["original_title"] = data.get("original_title")
    youtube_url = f'https://api.themoviedb.org/3/movie/{ data["id"] }/videos?api_key=c9ce586a25f99f5a58ec0e50547b7b7c&language=ko-KR'
    res_y = requests.get(youtube_url)
    res_y = res_y.json()
    for i in res_y.get('results'):
        if i.get('site') == 'YouTube' and i.get('type') == 'Trailer':
            fields['youtube'] = i.get('key')
  
    ###
    genres = []
    for i in range(len(data.get('genre_ids'))):
       genres.append(data['genre_ids'][i]) 
    fields["genres"] = genres
    url += f'{ data["id"] }/credits?api_key={key}'
    res = requests.get(url)
    res = res.json()
    a={}
    b = []
    for i in range(len(res.get('cast'))):
        if i > 4: break
        actor['pk'] = (idx*5)+i+1
        actor['model'] = 'movies.Actor'
        if res.get('cast')[i].get('profile_path'):
            a['profile_path'] = res.get('cast')[i].get('profile_path')
            a['name'] = res.get('cast')[i].get('name')
        actor['fields'] = a
        k = deepcopy(actor)
        actors.append(k)
        b.append((idx*5)+i+1)

    fields["actors"] = b
    movie["fields"] = fields
    movies.append(movie)


genres = []
for idx, data in enumerate(gdata.get('genres')):
    genre = {}
    field = {}
    genre['pk'] = data.get('id')
    genre['model'] = 'movies.genre'
    genre['fields'] = {"name" : data.get('name')}
    genres.append(genre)


with open('now_movie.json', 'w', encoding='utf-8') as make:
    json.dump(movies, make, indent='\t')

with open('now_genre.json', 'w', encoding='utf-8') as G:
    json.dump(genres, G, indent='\t')

with open('now_actor.json', 'w', encoding='utf-8') as A:
    json.dump(actors, A, indent='\t')