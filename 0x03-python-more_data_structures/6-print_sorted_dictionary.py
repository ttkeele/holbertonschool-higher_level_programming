#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for t in sorted(a_dictionary):
        print("{}: {}".format(t, a_dictionary[t]))
