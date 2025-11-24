import os
import csv
category = {
    'id': 'Id',
    'game': 'Game',
    'series': 'Series',
    'country': 'Country',
    'details': 'Details',
    'category': 'Ban Category',
    'status': 'Ban Status',
    'wikipedia': 'Wikipedia Profile',
    'image': 'Image',
    'summary': 'Summary',
    'developer': 'Developer',
    'publisher': 'Publisher',
    'genre': 'Genre',
    'homepage': 'Homepage'
}

# We created the menu layout for you
# Only given imports are allowed


def main(filename: str) -> None:
    games = load(filename)
    print("[I] Print request info from assignment")
    print("[M] Make modification based on assignment")
    print("[A] Add new game to list")
    print("[O] Overview of banned games per country")
    print("[S] Search the dataset by country")
    print("[Q] Quit program")
    # Implement rest of functionality
    choice = input("press corresponding button (after that enter)\n>").lower()
    if choice == 'q':
        quit()
    elif choice == 'i':
        banned = 0
        banned_amount = 0
        for row in games:
            if row['Country'] == 'Israel':
                banned += 1
        country_overview = Overview(games)
        for k, v in country_overview.items():
            if len(v) > banned_amount:
                banned_amount = len(v)
                country = k
        banned_of_series = search_by_series_or_game(games, "Assassin's Creed", 'Series')
        amount_banned = len(banned_of_series)
        games_in_country = search_by_country(games, 'Germany')
        Detail_a_country = search_by_series_or_game(games, 'Red Dead Redemption', 'Game')
        print(banned)
        print(country)
        print(amount_banned)
        for ban_game, Detail in games_in_country.items():
            print(f"{ban_game}\n{Detail}")
        for Country, Detail in Detail_a_country.items():
            print(f"{Country}\n{Detail}")
    elif choice == 'm':
        removed_germany = []
        for row in games:
            if row['Country'] != 'Germany':
                removed_germany.append(row)
        for row in removed_germany:
            if row['Game'] == 'Silent Hill VI':
                row['Game'] = 'Silent Hill Remastered'
            if row['Game'] == 'Bully' and row['Country'] == 'Brazil':
                row['Ban Status'] = 'Ban Lifted'
            if row['Game'] == 'Manhunt II':
                row['Genre'] = 'Action'
        dump(filename, removed_germany)
    elif choice == 'a':
        new_game = {}
        for item in category:
            value = input(f"what is the value of {item}\n>")
            new_game[category[item]] = value
        games.append(new_game)
        dump(filename, games)
    elif choice == 'o':
        country = Overview(games)
        for k, banned_games in country.items():
            print(f"{k} - {len(banned_games)}")
            for game in banned_games:
                print(f"- {game}")
    elif choice == 's':
        Country = input("what is the name of the country?\n>")
        games_in_country = search_by_country(games, Country)
        for ban_game, Detail in games_in_country.items():
            print(f"{ban_game} - {Detail}")


def load(filename):
    path = os.path.dirname(__file__)
    csv_file = os.path.join(path, filename)
    try:
        with open(csv_file, newline='', encoding="utf-8") as csvfile:
            games = list(csv.DictReader(csvfile))
            return games
    except FileNotFoundError as nf:
        print(f"File was not found: {nf}")


def dump(filename, games):
    path = os.path.dirname(__file__)
    csv_file = os.path.join(path, filename)
    try:
        with open(csv_file, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = list(category.values())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for game in games:
                clean_row = [{k: game.get(k, "") for k in fieldnames}]
                writer.writerows(clean_row)
    except FileNotFoundError as nf:
        print(f"File was not found: {nf}")


def Overview(games):
    country = {}    
    for row in games:
        c = row.get('Country')
        g = row.get('Game')
        if c not in country:
            country[c] = []
        if g not in country[c]:
            country[c].append(g)
    return country


def search_by_series_or_game(games, id_, type):
    if type == 'Series':
        games_in_serie = []
        for row in games:
            if (row['Game'] not in games) and (row['Series'] == id_):
                games_in_serie.append(row['Game'])
        return(games_in_serie)
    elif type == 'Game':
        Games_a_country = {}
        for row in games:
            if row['Game'] == id_:
                Games_a_country[row['Country']] = row['Details']
        return Games_a_country


def search_by_country(games, Country):
    games_in_country = {}
    for row in games:
        if row['Country'] == Country:
            games_in_country[row['Game']] = row['Details']
    return games_in_country


if __name__ == "__main__":
    while True:
        main("bannedvideogames.csv")