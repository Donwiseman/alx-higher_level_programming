#!/usr/bin/python3
def best_score(a_dictionary):
    big_value = 0
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for x, y in a_dictionary.items():
        if big_value < y:
            big_value = y
            best_score = x
    return best_score
