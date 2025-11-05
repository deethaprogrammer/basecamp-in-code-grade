"""
menu like:
[L] List users (sorted alphabetically by first name)
[S] Show friends of user (sorted alphabetically by first name)
[R] Recommend friends (sorted alphabetically by first name)
[Q] Quit program

---criteria---
social network is stored in friends.json

at startup the program reads the data of friends.json where the key is the user name and the value theire friends

A template file is provided that reads the data

users can:
list all users

show direct friends of a select user if tthe user has no friends their needs to be printed User has no friends.
if the user can't be found print Error: User not found.

recommend friends of friends excluding existing friends and the user self) including mutuak friend count in each recommendation
if there is no such user print Error: User not found
if the user exist but their is no friend to recommand pritn No Recommendation
if a username is not found display Error: user not found


prints and where

S: User has no friends. (if the user has no friends)
S: Error: User not found. (if its the wrong user name input)
R: Error: User not found. (if its the wrong user name input)
R: No Recommendation. (if their is no recommendation)
"""

import json

def load_social_network(filename):
    """
    Loads the social network from a JSON file and returns a dictionary
    where keys are usernames and values are sets of direct friends.
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            network = {}
            for user, friends in data.items():
                network[user] = set(friends)
            return network
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return {}

def list_users(network):
    """
    Lists all users in the network, sorted alphabetically.
    """
    names = []
    full_name = []
    for x in network.keys():
        part = x.split()
        first = part[0]
        last = " ".join(part[1:])
        names.append((first, last))
    names.sort(key=lambda name: (name[0].lower(), name[1].lower()))
    for name in names:
        full_name.append(" ".join(name))
    return print(",\n".join(full_name))

def show_friends(user, network):
    """
    Shows direct friends of the specified user.
    If user is not found, prints an error message: Error: User not found.
    """
    if len(network[user]) == 0:
        return print("User has no friends.")
    return print(',\n'.join(sorted(network[user])))

def recommend_friends(user, network):
    """
    Recommends friends of friends for a user, excluding their current friends and self.
    Displays mutual friend count for each recommendation.
    """
    rec_names = []
    rec_friends = {}
    rec_Friend = []
    friends_name = network[user]
    print(friends_name)
    for names in friends_name:
        for name in network[names]:
            if name != user and not name in friends_name:
                if name in rec_friends:
                    rec_friends[name] += 1
                else:
                    rec_friends[name] = 1
    for x in rec_friends.keys():
        part = x.split()
        first = part[0]
        last = " ".join(part[1:])
        rec_names.append((first, last))
    rec_names.sort(key=lambda name: (name[0].lower(), name[1].lower()))
    for name in rec_names:
        rec_Friend.append(" ".join(name))
    if len(network[user]) >0:
        return print("Recommended friends for " + user + ":\n-" + "\n-".join(f"{rec_name} ({rec_friends[rec_name]} mutual friends)" for rec_name in rec_Friend))
    else:
        return print("No Recommendation.")
    # todo: finish the body
    
def Menu(choice, network):
    if choice == 'L':
        return list_users(network)
    elif choice == 'S':
        user = input("Enter username: ")
        if user not in network.keys():
            return print("Error: User not found.")
        return show_friends(user, network)
    elif choice == 'R':
        user = input("Enter username: ")
        if user not in network.keys():
            return print("Error: User not found.")
        return recommend_friends(user, network)
    elif choice == 'Q':
        quit()
    else:
        return print('wrong input')

def main():
    filename = __file__.replace("\\", "/").rsplit("/", 1)[0] + "/friends.json"
    network = load_social_network(filename)
    while True:
        # todo: finish the body
        menu = input("[L] List users (sorted alphabetically)\n[S] Show friends of user (sorted alphabetically)\n[R] Recommend friends (sorted alphabetically)\n[Q] Quit program\n>").upper()
        Menu(menu, network)

if __name__ == "__main__":
    main()