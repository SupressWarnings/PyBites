from collections import Counter

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automakers = [entry["automaker"] for entry in data if entry["year"] == year]
    scoreboard = set(automakers)
    score_dict = {automaker: 0 for automaker in scoreboard}
    for car in automakers:
        score_dict[car] += 1
    return max(score_dict, key=lambda x: score_dict[x])


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set(
        [
            entry["model"]
            for entry in data
            if entry["automaker"] == automaker and entry["year"] == year
        ]
    )

