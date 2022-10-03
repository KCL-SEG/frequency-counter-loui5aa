"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from operator import truediv


def frequencies(items):
    frequencies = {}
    for x in items:
        if len(frequencies) == 0: #if dictionary empty
            frequencies[str(x)]=1
        else: #if dictionary has contents
            founditem = 0
            for y in frequencies:
                if x == y: #if the item is in the dictionary
                    frequencies[y]=+ 1
                    founditem = 1
            if founditem == 0:
                frequencies[str(x)] = 1
    print("Loading done")
    return frequencies
