import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = "/tmp"

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movie_dict = csv.DictReader(open(local))
    movies = {}
    for row in movie_dict:
        director = row.pop("director_name")
        title = row.pop("movie_title")
        year = row.pop("title_year")
        score = row.pop("imdb_score")
        if director != "" and title != "" and year != "" and score != "":
            int_year = int(year)
            float_score = float(score)
            movie = Movie(title, int_year, float_score)
            if director not in movies.keys():
                movies[director] = []
            if int_year >= 1960:
                movies[director].append(movie)
    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(sum([movie.score for movie in movies]) / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    list = [
        (director, calc_mean_score(directors[director]))
        for director in directors.keys()
    ]
