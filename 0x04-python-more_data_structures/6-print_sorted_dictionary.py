#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortList = sorted(a_dictionary.keys())
    for k in sortList:
        print("{:s}: {}".format(k, a_dictionary[k]))
