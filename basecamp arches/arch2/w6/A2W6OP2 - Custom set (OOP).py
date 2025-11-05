def create_set(*args) -> list:
    """
    Creats a custom set with the given items.
    """
    my_set: list = []

    # For each argument given to the set:
    for item in args:

        # If it's not in the current set:
        if item not in my_set:

            # Add it to the current set
            my_set.append(item)

    return my_set


def has(my_set: list, item) -> bool:
    """
    Returns `True` if the item exists in this set, `False` otherwise.
    """
    return item in my_set


def add(my_set: list, item) -> None:
    """
    Adds the item to the set iff the item isn't in the set already.
    """
    if item not in my_set:
        my_set.append(item)
    pass


def remove(my_set: list, item) -> None:
    """
    Removes the item from the set if the item is in the set.
    """
    if item in my_set:
        my_set.remove(item)
    pass


def union(my_set: list, other_set: list) -> list:
    set_copy = my_set.copy()
    for item in other_set:
        if item not in set_copy:
            set_copy.append(item)
    return set_copy


def intersect(my_set: list, other_set: list) -> list:
    """
    Returns a new custom set that contains the intersection of two sets.
    """
    intersect_set = []
    for item in my_set:
        if item in other_set:
            if item not in intersect_set:
                intersect_set.append(item)
    return intersect_set