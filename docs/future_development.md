# Future Development

Possibly ways to extend this project:

- Look at getting data out to a CSV rather than just printing.
- Filter or group words by part of speech.
- Rather than just returning the words, actually substitute in the related characters with actual "py" characters.
- After getting results, select a few and search the Python Package Index or Github to see if they are in use already or not.
- Expect an input word and return its synonyms which are suitable for the "py" pattern.
- Allow easy to customise pattern for other purposes like generating a name for band or company, based on partial match of the a word in another word. Consider using string similarity dfifference or simple one-character difference calculation e.g. find a word which contains the search term except the search term can have one letter different. Or certain characters like `s`/`z` and `c`/`k` are interchangeable.
- Unix systems have a builtin dictionary - use that instead of a REST API.
- See also dumps like https://github.com/adambom/dictionary
