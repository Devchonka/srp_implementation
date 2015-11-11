"""
@author: Elena Menyaylenko
Homework #3.

Merging dictionaries with identical keys. If the same input key shows up in several dictionaries to merge,
the merged dictionary should contain a list of all the corresponding values for that input.
"""

from collections import Iterable


def main():
    """
    This function will unwrap any number of passed dictionaries and call a function to merge them, one by one.
    It starts by creating a merged dictionary object of None, which inside another functions turns into a dict.
    :return: printed final dictionary of all the merged dictionaries
    """
    dict_tuple = createDicts()
    merged_dict = None

    print('\n The starting dictionaries are:')
    for iter in dict_tuple:
        print(iter)
        merged_dict = merge_2_dicts(merged_dict, iter)

    print('\n The merged final dictionary is:')
    print(merged_dict)


def createDicts():
    """
    This function hardcodes some dictionaries and returns as a tuple to the caller.
    """
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'b': 2, 'c': 250, 'd': 0, 'e': 0}
    dict4 = {'a': 0, 'b': 2}
    return dict1, dict2, dict3, dict4


def merge_2_dicts(merged_dict, dict2):
    """

    :param merged_dict: The dictionary that currently contains a merged variation of all previous dicts
    :param dict2: the dictionary which contains values and keys to append
    :return: a varied copy of merged_dict with added values, repeats are appended as a list to current keys
    """
    if merged_dict is None:
        merged_dict = {}

    for key in dict2:
        if key not in merged_dict:
            merged_dict[key] = dict2[key]
        else:
            if isinstance(merged_dict[key], Iterable):
                merged_dict[key].append(dict2[key])
            else:
                merged_dict[key] = [merged_dict[key]]
                merged_dict[key].append(dict2[key])
    return merged_dict


if __name__ == '__main__':
    main()

""" OUTPUT:
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk3 $ python3 main.py

 The starting dictionaries are:
{'b': 2, 'a': 1}
{'c': 4, 'b': 3}
{'e': 0, 'c': 250, 'b': 2, 'd': 0}
{'b': 2, 'a': 0}

 The merged final dictionary is:
{'e': 0, 'c': [4, 250], 'b': [2, 3, 2, 2], 'a': [1, 0], 'd': 0}
elena@elena-e5250 ~/PycharmProjects/PythonCourse/Hwk3 $

"""