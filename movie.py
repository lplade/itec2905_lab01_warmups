#!/bin/python

# Write a program that fetches data from a web server using an open API. Ask me
# for the server you should use and the specific data you should fetch.
#
# You'll need to do some research into how to carry out these tasks in Python.
# (Hint: the requests library)
#
# Your Python program will make a request to the website, and get data as JSON.
# You'll need to process this to extract the data you need.
#
# You should handle errors, such as access denied, no network connection,
# invalid response....
#
# Extra challenge: your program should cache data locally to avoid excessive
# requests. If the user has made a request recently, your program should fetch
# the data from the cache instead of the website.

import requests
# import json

movie_string = input("Enter a movie to get a rating for: ")
# TODO validate this
# TODO convert whitespace etc to url codes (%20)

# Parameters that get passed into query
payload = {
    't': movie_string,  # does this encode our whitespace?
    'type': 'movie'
}

r = requests.get("http://www.omdbapi.com/?", params=payload)

# TODO test HTTP status of request, handle that
r.raise_for_status()

# send the request json to the json parser
parsed_json = r.json()

# print(parsed_json)

# access the relevant keys in the dict
matched_title = parsed_json['Title']
rating = parsed_json['imdbRating']

print("IMDB Rating for " + matched_title + " is " + str(rating))

# docs for json library
# http://docs.python-guide.org/en/latest/scenarios/json/

# docs for request library
# http://docs.python-requests.org/en/master/user/quickstart/#json-response-content



