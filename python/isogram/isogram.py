def is_isogram(string):
    # Turn string into a list of characters
    string = string.upper()
    stringList = get_characters(string)

    # Remove spaces, hyphens etc.
    toRemove = ['-', ' ']
    stringList = [i for i in stringList if i not in toRemove]

    # If the length of the set doesn't equal the length of the string, then
    # there is repetition
    stringLength = len(stringList)
    unique = len(set(stringList))

    if stringLength != unique:
        return False
    else: 
        return True


def get_characters(word): 
    # Turns a string into a list of characters
    return [char for char in word]  