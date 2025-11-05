"""
menu:
[1] Print the number of TV Shows
[2] Print the number of Movies
[3] Print the (full) names of directors in alphabetical order who directed both TV shows and movies.
    (for example, search the name David Ayer. He is the director of three movies and one tv show)
    Treat multiple directors (separated by comma) as 1 single director!
[4] Print the name of each director in alphabetical order,
    the number of movies and the number of tv shows (s)he was the director of.
    Use a tuple with format: (director name, number of movies, number of tv shows) to print.

---criteria---
The program gets the file name as a program argument.

Use the function load_csv_file to load the content of the file in a list.

The first line of the file specifies the name of each column.
For example, the first column is show_id, the second is the type of the show, etc...
Create a function called get_headers(file_content) that returns a list of all the columns from
the first row (explore the kind of information you can extract)
Make a function search_by_type(file_content, show_type) that returns a list of 
all TV Shows or Movies based on the requested type
    Make use of lambda for the solution

Make a function search_by_director(file_content, director)
that returns a list of all TV Shows and Movies that have that director
    Make use of lambda for the solution

Make a function get_directors(file_content) that returns a set of directors in the list (use set for single directors only)
    Treat multiple directors (separated by comma) as 1 single director!
"""
import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []
    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))
    return file_content


def get_headers(file_content):
    return file_content[0]


def search_by_type(file_content, show_type):
    file_content = header(file_content)
    media = []
    for item in file_content:
        if item["type"] == show_type:
            media.append(item)
    return media


def get_directors(file_content):
    file_content = header(file_content)
    director = set()
    for item in file_content:
        name = item["director"]
        if name:
            director.add(name.strip())
    return sorted(director, key=lambda name: (name.split()[0], name.split()[-1]))


def dir_movie_and_tv(data, directors):
    file_content = header(data)
    dir_list_creation = []
    for director in directors:
        movies = 0
        tv_count = 0
        for item in file_content:
            if item["director"] == director:
                if item["type"] == 'Movie':
                    movies += 1
                elif item["type"] == 'TV Show':
                    tv_count += 1
        dir_list_creation.append((director, movies, tv_count))
    has_both = [director for director, movies, tv_count in dir_list_creation if movies > 0 and tv_count > 0]
    return has_both


def director_movie_tv_count(data, directors):
    file_content = header(data)
    dir_list_creation = []
    for director in directors:
        movies = 0
        tv_count = 0
        for item in file_content:
            if item["director"] == director:
                if item["type"] == 'Movie':
                    movies += 1
                elif item["type"] == 'TV Show':
                    tv_count += 1
        dir_list_creation.append((director, movies, tv_count))
    return dir_list_creation


def menu(number, data):
    if number == "1":
        return print(len(search_by_type(data, "TV Show")))
    if number == "2":
        return print(len(search_by_type(data, "Movie")))
    if number == "3":
        directors = get_directors(data)
        has_both = dir_movie_and_tv(data, directors)
        return print(has_both)
    if number == "4":
        directors = get_directors(data)
        director_made = director_movie_tv_count(data, directors)
        return print(director_made)
    pass


def header(data):
    header = get_headers(data)
    list_of_items = []
    for item in data[1:]:
        info = {key: value for key, value in zip(header, item)}
        list_of_items.append(info)
    return list_of_items


def search_by_director(file_content, director):
    file_content = header(file_content)
    movies_by_director = []
    for item in file_content:
        if item["director"] == director:
            movies_by_director.append(item)
    return movies_by_director


if __name__ == "__main__":
    file_content = load_csv_file("netflix_titles.csv")
    menu_choice = input("[1] Print the number of TV Shows\n[2] Print the number of Movies\n[3] Print the (full) names of directors in alphabetical order who directed both TV shows and movies.\n[4] Print the name of each director in alphabetical order, the number of movies and the number of tv shows (s)he was the director of.\n>")
    menu(menu_choice, file_content)