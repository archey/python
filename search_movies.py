#!/usr/bin/python

from imdb import IMDb

ia = IMDb()

query = raw_input("Please input Movie Name" + " ")

def search(query):
    result = ia.search_movie(query)
    for item in result:
        print type(result)
        print item
        print item['long imdb canonical title'], item.MovieID



search(query)
