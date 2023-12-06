#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = list(set(my_list))
    list_length = len(new)
    summation = 0
    for i in range(list_length):
        summation = summation+new[i]
return(summation)
