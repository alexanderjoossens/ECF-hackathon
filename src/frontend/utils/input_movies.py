import os
import random
import itertools
import csv
import pandas as pd

def get_movie_title_list():
    movie_title_list = [
        "The Lion King",
        "Pulp Fiction",
        "Harry Potter and the Philosopher's Stone",
        "The Notebook",            
        "The Social Network",                
        "The Godfather",       
        "The Fast and the Furious: Tokyo Drift",    
        "Home Alone",              
        "Saw",                 
        "The Shawshank Redemption",                  
    ]
    return movie_title_list

def get_movie_poster_list():
    print(get_movie_index_list())
    return [get_movie_poster_path(movie_title) for movie_title in get_movie_index_list()]

def get_movie_genres_list():
    a = [get_movie_genres(movie_title) for movie_title in get_movie_index_list()]
    print('a')
    print(a)
    return [get_movie_genres(movie_title) for movie_title in get_movie_index_list()]

def get_movie_index_list():
    return [get_movie_index(movie_title) for movie_title in get_movie_title_list()]

def get_random_movie_title():
    filesize = 10000  # size of the really big file
    offset = random.randrange(filesize)

    csv_path = os.path.join(os.getcwd(), '..', "..", 'title_export.csv')

    f = open(csv_path)

    f.seek(offset)  # go to random position
    f.readline()  # discard - bound to be partial line
    random_line = f.readline()  # bingo!

    # extra to handle last/first line edge cases
    if len(random_line) == 0:  # we have hit the end
        f.seek(0)
        random_line = f.readline()  # so we'll grab the first line instead

    f.close()

    return random_line

def get_csv_line(path, line_number):
    with open(path) as f:
        return next(itertools.islice(csv.reader(f), line_number, None))

def get_movie_title(index):
    csv_path = os.path.join(os.getcwd(), '..', "..", 'title_export.csv')
    return get_csv_line(csv_path, index + 2)

def get_movie_index(title):
    csv_path = os.path.join(os.getcwd(), '..', "..", 'title_export.csv')

    with open(csv_path, encoding="utf8") as f:
        csv_file = csv.reader(f, delimiter=",")
        for row in csv_file:
            if row[0] == title:
                return row[1]

def get_movie_poster_path(index):
    csv_path = os.path.join(os.getcwd(), '..', "..", 'poster_path_export.csv')
    row = None  # Initialize row to ensure it's assigned

    try:
        with open(csv_path, encoding="utf8") as f:
            csv_file = csv.reader(f, delimiter=",")
            for i, row in enumerate(csv_file):
                if i - 1 == int(index):
                    break
            else:
                row = None  # Handle the case where the index is not found

        if row is not None:
            return row
        else:
            print(f"Index '{index}' not found in {csv_path}")
            return None
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return None

def get_movie_genres(index):
    csv_path = os.path.join(os.getcwd(), '..', "..", 'movie_genres_export.csv')
    row = None  # Initialize row to ensure it's assigned

    try:
        with open(csv_path, encoding="utf8") as f:
            csv_file = csv.reader(f, delimiter=",")
            for i, row in enumerate(csv_file):
                if i - 1 == int(index):
                    break
            else:
                row = None  # Handle the case where the index is not found

        if row is not None:
            return row
        else:
            print(f"Index '{index}' not found in {csv_path}")
            return None
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return None
