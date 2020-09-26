# Logic

This document includes logic which has been implemented or is intended to be implemented.


## Rules

Dataset: English dictionary. Possibly prioritize nouns, verbs and adjectives in that order, followed by the other parts of speech. 

Well-known or common words are preferred.

Proper nouns are allowed.

Length: 3 to 15 characters (change based on results)

Pattern match: Match any condition to add it to the collection, with a match on a higher rule as most likely to be suitable. A word with py in it is probably good. Words with a 'p' and one or two consequetive vowels which could be replaced with 'py'. The subsitutition might not be done in the project itself, but the idea is to give words where this subsitution could be done.

Possibly check against PyPi to see if a word is taken with out without py substitution done.

## Patterns

Placement - prioritise start with, then ends with and then contains.
Letters to match)
 - 'py'
 - 'p'
 - 'p' and a vowel or y and non-vowel (consonant or end of word)
 - 'p' and a vowel or y and then another vowel or y
 - a word which does not contain py but can have it inserted possibly at the start or end. e.g. existing "PyDictionary" package. Though these are probably too obvious, unless it was generated for synonyms of a chosen word.
 
## Process

1. Get all suitable words and their attributes.
2. Prefilter based on length and part of speech.
3. Iterate through words.
4. Test a word against all the conditions. Which rules it matches, giving weighting scores possibly. If at least one rule is matched, show.
5. Print to screen (or a sample or filtered view if on a command-line tool expecting short output, otherwise write to CSV.
6. Optionally include the definitions or part of speech.
