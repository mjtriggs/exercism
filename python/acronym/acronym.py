def abbreviate(words):
    # Clean string by removing any punctuation
    words = words.replace('-', ' ')
    words = words.replace('_', ' ')
    
    # Split the string into seperate words in the list
    words = words.upper().split()
    output = [get_first_letter(word) for word in words]
    output = ''.join(output)
    return output

def get_first_letter(word):
    return word[0]