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
    """
    Expect a word and return True if is valid or False otherwise.

    Validate word on length and not starting or ending with punctuation.
    """
    return all(
        (
            5 <= len(word) <= 10,
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
# Useful for testing to get the same results each time when JSON is converted
# to a dict. But unnecessary in final app.
words = sorted(words)

# TODO: Add re.IGNORECASE throughout.

# Rules are written to be as narrow as possible, such that the part of word
# which has a 'p' in it will be allocated to one of the groupings or none
# at all. However, the word can existing in multiple groupings, if the
# letter 'p' appears in the word multiple times and they match different rules.
groupings = {
    'p_and_ee_sound': {
        'start': {
            'pattern': re.compile(r"^p((ea)|(ee)|(ie)|(ye)).+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p((ea)|(ee)|(ie)|(ye)).+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p((ea)|(ee)|(ie)|(ye))$"),
            'matches': []
        },
        'replace_pattern': re.compile(r"p((ea)|(ee)|(ie)|(ye))")
    },
    'p_vowel_y': {
        'start': {
            'pattern': re.compile(r"^p[aeo]y.+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[aeo]y.+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+.p[aeo]y$"),
            'matches': []
        },
    },
    # The letter between the 'p' and the 'y' could be removed to change
    # the sound of the word. This relates to the rule above.
    'p_something_y': {
        'start': {
            'pattern': re.compile(r"^p[^aeo]y+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[^aeo]y.+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[^aeo]y$"),
            'matches': []
        },
    },
    'py_then_vowel': {
        'start': {
            'pattern': re.compile(r"^py[aeiouy].+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+py[aeiouy].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+py[aeiouy]$"),
            'matches': []
        },
    },
    # This also covers words ending in py.
    'py_then_no_vowel': {
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
    # Single vowel after a 'p' and the sound should be natural when it is
    # replaced by a y.
    'p_and_natural_vowel': {
        'start': {
            'pattern': re.compile(r"^p[ei][^aeiouy].+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[ei][^aeiouy].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[ei]$"),
            'matches': []
        },
    },
    # Single vowel after a 'p' and the sound will probably sound forced
    # when it is replaced by a y. But perhaps there will be something useful
    # in here. The end pattern matches on a consonant or end of word.
    'p_and_forced_vowel': {
        'start': {
            'pattern': re.compile(r"^p[aou][^aeiouy]+"),
            'matches': []
        },
        'middle': {
            'pattern': re.compile(r".+p[aou][^aeiouy].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[aou][^aeiouy]?$"),
            'matches': []
        },
    },
    # Note that for this grouping, there is no pattern looking for the
    # middle of the word, as it would be too broad to be useful.
    # The end pattern matches on a consonant or end of word.
    'p': {
        'start': {
            'pattern': re.compile(r"^p[^aeiouy].+"),
            'matches': []
        },
        'end': {
            'pattern': re.compile(r".+p[^aeiouy]?$"),
            'matches': []
        },
    },
    # A 'p' could be added in front of this.
    'starts_with_y': {
        'start': {
            'pattern': re.compile(r"^y.+"),
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
            if group != 'p_and_ee_sound':
                continue
            for position, values in positions.items():
                if position == 'replace_pattern':
                    continue
                if values['pattern'].search(word):
                    # Get the replace_pattern from a level up.
                    replace_pattern = positions.get('replace_pattern', None)
                    if replace_pattern is not None:
                        modified_word = replace_pattern.sub('py', word)
                    else:
                        modified_word = None

                    values['matches'].append(
                        (word, modified_word)
                    )

for group, positions in groupings.items():
    print(group)
    print("========")
    for position, values in positions.items():
        if position == 'replace_pattern':
            continue
        print(position)
        print("-------")
        matches = values['matches']
        print(len(matches))
        # Sort by length of word after subsitution.
        print(sorted(matches, key=lambda x: len(x[1]))[:20])
        print()
    print()

# TODO: Change structure to use keys for replaced words and then values
# as the words which were used to get to it.
# It can be across all groups as we care about the result, but still
# split into start/middle/end. Or maybe include the groupings to see how
# it got to that (should be one but could be multiple).

# TODO: Add more replace patterns.
