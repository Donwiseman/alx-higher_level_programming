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


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
