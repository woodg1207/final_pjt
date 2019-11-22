import json
from pprint import pprint
with open('now_playing.json','r', encoding='UTF8') as f:
    jdata = json.load(f)

movies = []
for idx, data in enumerate(jdata.get("results")):
    # print(data.get("title"))
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
    movie["fields"] = fields
    movies.append(movie)

# pprint(movies)
with open('now.json', 'w', encoding='utf-8') as make:
    json.dump(movies, make, indent='\t')