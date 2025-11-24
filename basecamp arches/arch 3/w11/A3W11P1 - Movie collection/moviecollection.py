import os
import json

# We created the menu layout for you
# Only given imports are allowed


def main() -> None:
    print("[I] Movie information overview")
    print("[M] Make modification based on assignment")
    print("[S] Search a movie title ")
    print("[C] Change title and/or release year by search on title")
    print("[Q] Quit program")

    # Implement rest of functionality


def load_json():
    path = os.path.dirname(__file__)
    json_file = os.path.join(path, "movies.json")
    try:
        with open(json_file, "r", encoding="utf-8") as r:
            movies = json.load(r)
        return movies
    except FileNotFoundError as nf:
        print(f"file is not found: {nf}")
    return None


def menu(menu_choice, movies):
    if menu_choice == "q":
        quit()
    elif menu_choice == "i":
        total_movies_2004 = num_movie(movies, 'year', 2004)
        total_movies_SF = num_movie(movies, 'genres', 'Science Fiction')
        toa1 = movies_with(movies, 'cast', 'Keanu Reeves')
        toa2 = movies_with(movies, 'cast', 'Sylvester Stallone', (1995, 2005))
        return total_movies_2004, total_movies_SF, toa1, toa2
    elif menu_choice == "m":
        movies = Change_title(movies, 'Gladiator', None, 2001)
        oldest_movie = search_oldest(movies)
        print(oldest_movie)
        for movie in movies:
            if movie['year'] == oldest_movie:
                oldest_movie = movie
                break
        movies = Change_title(movies, oldest_movie['title'], None, oldest_movie['year'] - 1)
        movies = name_change(movies, 'Natalie Portman', 'Nat Portman')
        movies = name_change(movies, 'Kevin Spacey')
        dumping(movies)
    elif menu_choice == "s":
        title = input("what is the title name of the movie you want to find?\n>")
        return search_movie(movies, title)
    elif menu_choice == "c":
        title = input("what is the title name of the movie you want change?\n>")
        new_title = input("what is the new name?\n>")
        new_year = input("what is the new year?\n>")
        movies = Change_title(movies, title, new_title, new_year)
        dumping(movies)


def search_movie(movies, title):
    for movie_dict in movies:
        if movie_dict['title'] == title:
            return movie_dict
    return "movie not found"


def name_change(movies, old_name, new_name=None):
    for movie in movies:
        if old_name in movie['cast']:
            movie['cast'].remove(old_name)
            if new_name is not None:
                movie['cast'].append(new_name)
    return movies


def num_movie(movies, Type, info):
    length = 0
    for movie_data in movies:
        if isinstance(movie_data[Type], list):
            if info in movie_data[Type]:
                length += 1
        else:
            if info == movie_data[Type]:
                length += 1
    return length


def movies_with(movies, Type, info, range=None):
    if range is not None:
        from_year, to_year = range
    movie_list = []
    for movie_data in movies:
        if (info in movie_data[Type]) and (range is None):
            movie_list.append(movie_data['title'])
        elif (info in movie_data[Type]) and (range is not None):
            if from_year <= movie_data['year'] <= to_year:
                movie_list.append(movie_data['title'])
    return movie_list


def dumping(movies):
    path = os.path.dirname(__file__)
    json_file = os.path.join(path, "movies.json")
    try:
        with open(json_file, "w", encoding="utf-8") as d:
            json.dump(movies, d, indent=4)
    except FileNotFoundError as nf:
        print(f"file is not found: {nf}")
    return None


def search_oldest(movies):
    oldest = None
    for movie in movies:
        if oldest is None or movie['year'] < oldest:
            oldest = movie['year']
    return oldest


def Change_title(movies, title, new_title=None, new_year=None):
    for movie_data in movies:
        if movie_data['title'] == title:
            if new_title is not None:
                movie_data['title'] = new_title
            if new_year is not None:
                movie_data['year'] = new_year
    return movies


if __name__ == "__main__":
    while True:
        main()
        movies = load_json()
        menu_choice = input(">").lower()
        returns = menu(menu_choice, movies)
        if returns is not None:
            if not isinstance(returns, dict):
                for item in returns:
                    print(item)
            else:
                print(returns)