#!/usr/bin/env python3
"""
Main application.
"""
import json
import re


# TODO: This from a dictionary repo on Github. Refine this approach,
# possibly with a different source.
DICTIONARY_PATH = "/home/michael/public_repos/dictionary/dictionary.json"


def verify(word):
    """Expect a word and return True if is valid or False otherwise.

    Validate word on length and not starting or ending with punctuation.
    """
    return all(
        (
            4 <= len(word) <= 10,
            word[0].isalpha(),
            word[-1].isalpha()
        )
    )


with open(DICTIONARY_PATH) as f_in:
    data = json.load(f_in)

# This is a generator, not a list. So it cannot be sliced but it is efficient
# to iterate over.
words = data.keys()
# TEMP
# Useful for testing to get the same results each time when JSOS is converted
# to a dict. But unnecessary in final app.
words = sorted(words)

# Rules are enforced such that they are mutually exclusive. Which means that
# having a p and single vowel means the next letter is not a vowel. And the p
# group means there is no vowel or y after the p. However, if a word has
# multiple p letters in it, the word could be allocated to one group for one
# rule and also another group for another rule, so there could be duplicates.
# Omit matches for just a p in the middle, which is too broad.
groupings = {
    'p_vowel_y': {
        'start': {
            'pattern': re.compile(r"^p[aeiou]y.+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[aeiou]y.+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[aeiou]y$"),
            'matches': []
        },
    },
    'p_y_vowel': {
        'start': {
            'pattern': re.compile(r"^py[aeiou].+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+py[aeiou].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+py[aeiou]$"),
            'matches': []
        },
    },
    'p_double_vowel': {
        'start': {
            'pattern': re.compile(r"^p[aeiou]{2}.+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[aeiou]{2}.+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[aeiou]{2}$"),
            'matches': []
        },
    },
    'p_vowel': {
        'start': {
            'pattern': re.compile(r"^p[aeiou].+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[aeiou].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[aeiou]$"),
            'matches': []
        },
    },
    'py': {
        'start': {
            'pattern': re.compile(r"^py[^aeiouy].+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+py[^aeiouy].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+py[^aeiouy]$"),
            'matches': []
        },
    },
    'p': {
        'start': {
            'pattern': re.compile(r"^p[^aeiouy].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p$"),
            'matches': []
        },
    },
}


# This could be faster as list comprehension but harder to write out.
# An efficiency is not so important for once off generation output for
# a few seconds.
for word in words:
    word = word.lower()

    if verify(word):
        for group, positions in groupings.items():
            for position, values in positions.items():
                if values['pattern'].search(word):
                    values['matches'].append(word)

for group, positions in groupings.items():
    print(group)
    print("========")
    for position, values in positions.items():
        print(position)
        print("-------")
        matches = values['matches']
        print(len(matches))
        print(sorted(matches, key=len)[:20])
        print()
    print()
