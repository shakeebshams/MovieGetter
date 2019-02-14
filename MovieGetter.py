#!/usr/bin/env python3
import requests
__author__ = """Shakeeb Shams"""

"""
Get an account from themoviedb.org. Go to this link and create an account:
https://www.themoviedb.org/?_dc=1489731496
assign your API key to the variable below
"""

API_KEY = "please enter API key within the quotes"
base_url = "https://api.themoviedb.org/3/movie/"

"""
Function name: get_movie_recommendations
Parameters: movie_ids (list of ints)
Returns: recommended movie titles (list of strings)
"""

def get_movie_recommendations(movie_ids):
    newlist = []
    for x in movie_ids:
        r = requests.get(base_url + "{}?api_key=".format(x) + API_KEY)
        data = r.json()
        if len(data) > 2:
            if data["popularity"] > 20:
                newlist.append(data["title"])
    return(newlist)
"""
Function name: get_upcoming
Parameters: None
Returns: the next 10 upcoming movies titles (list of strings)
"""

from pprint import pprint
def get_upcoming():
    upcoming_list = []
    r = requests.get("https://api.themoviedb.org/3/movie/upcoming?api_key=+" + "Your KEY here" + "&language=en-US&page=1")
    data = r.json()
    pprint(data)
    arb = data["results"]
    for x in arb:
        if len(upcoming_list) < 10:
            upcoming_list.append(x["title"])
    return(upcoming_list)


"""
Function name: get_cast_members
Parameters: movie_id (int), job_title (string), section (string)
Returns: names of people who worked the job specified by the job title for the
given movie (list of strings)

"""


def get_cast_members(movie_id, job_title, section):
    newlist = []
    r = requests.get("https://api.themoviedb.org/3/movie/{}/credits?api_key=5fcbeae436c656f9e7f98b5c6d06063f".format(movie_id))
    data = r.json()
    if section == "cast":
        for x in data["cast"]:
            newlist.append(x["name"])
        return(newlist)
    elif section == "crew":
        for x in data["crew"]:
           if x["job"] == job_title:
                newlist.append(x["name"])
        return(newlist)

"""
Function name: map_movies_to_language
Parameters: movie_ids (list of ints), languages (list of strings)
Returns: a dictionary mapping languages to the movies titles available in that
language
"""


def map_movies_to_languages(movie_ids, languages):
    newdict = {}
    for x in languages:
        newlist = []
        golist = []
        for y in movie_ids:
            r = requests.get("https://api.themoviedb.org/3/movie/{}/translations?api_key=5fcbeae436c656f9e7f98b5c6d06063f".format(y))
            data = r.json()
            if "status_code" in data.keys():
                continue
            arb = data["translations"]
            for lit in arb:
                if lit["english_name"] == x:
                    newlist.append(y)
        for helu in newlist:
            r = requests.get(base_url + "{}?api_key=".format(helu) + API_KEY)
            data = r.json()
            if len(data) > 2:
                if data["title"] not in golist:
                    golist.append(data["title"])
        newdict[x] = golist
    return(newdict)



"""
Function name: get_genre_movies
Parameters: movie_ids (list of ints), genre (string), start_year (int),
end_year (int)
Returns: movie titles (list of strings)
"""


def get_genre_movies(movie_ids, genre, start_year, end_year):
    newlist = []
    for x in movie_ids:
        r = requests.get(base_url + "{}?api_key=".format(x) + API_KEY)
        data = r.json()
        if len(data) <= 2:
            continue
        sircut = data["genres"]
        for y in sircut:
            if y["name"] == genre:
                date = data["release_date"]
                date = date.split("-")
                if int(date[0]) > start_year:
                    if int(date[0]) < end_year:
                        newlist.append(data["title"])
    return(newlist)
