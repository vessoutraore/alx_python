#!/usr/bin/python3
# update dictionary if key exist otherwirse add to dicationatry
#the two return was neccessary for the bug fix comon


def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) == 0:
       a_dictionary[key] = value
    #    print_sorted_dictionary(a_dictionary)
    else:
        for k, v in a_dictionary.items():
            if key in k == True:
                a_dictionary[key] = value
            else:
                a_dictionary[key] = value
            return a_dictionary
    return a_dictionary
