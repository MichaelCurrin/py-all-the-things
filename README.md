# Py All The Things
_Find English words which could easily have "py" substituted in them, to help generate Python package names (Python3 terminal tool)_

This project is a tool to generate Python package project names which follow the style of using "py" in the title. It is intended for use by other Python developers who are looking for names for their new projects. The idea is inspired by working with project with names such as _PyDictionary_, _Jupyter_ or _tweepy_ and realising their must be a systematic way to find words like those.

The logic is to iterate through all words in the English language, exclude the words which are too long or short and filter to the words following the required pattern.

Possibly ways to extend this project:

- Look at getting data out to a CSV rather than just printing.
- Filter or group words by part of speech.
- Rather than just returning the words, actually subsitute in the related characters with actual "py" characters.
- After getting results, select a few and search the Python Package Index or Github to see if they are in use already or not.
- Expect an input word and return its synonyms which are suitable for the "py" pattern.
- Allow easy to customise pattern for other purposes like generating a name for band or company, based on partial match of the a word in another word. Consider using string similarity dfifference or simple one-character difference calculation e.g. find a word which contains the search term except the search term can have one letter different. Or certain characters like s/z and c/k are interchangeable.
