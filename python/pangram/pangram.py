import re

def is_pangram(sentence):
    '''
    Function to determine if a sentence is a pangram. A pangram is a sentence that contains every letter of the alphabet.
    '''
    # Make sentence upper case and remove white space
    sentence = sentence.upper()
    sentence = sentence.replace(" ", "")
    sentence = re.sub(r'[^A-Z]','',sentence)

    # Create set and check the length
    uniques = len(set(sentence))

    return uniques == 26