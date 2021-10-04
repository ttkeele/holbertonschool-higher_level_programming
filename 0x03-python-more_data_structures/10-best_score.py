#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    trent = keys[0]
    for i in keys:
        trent = i if a_dictionary[i] > a_dictionary[trent] else trent
    return trent
