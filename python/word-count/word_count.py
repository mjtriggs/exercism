import re

def count_words(sentence):
    # Function to count the number of distinct words in a phrase.

    # change everything to lower case
    sentence = sentence.lower()

    # Remove punctuation
    sentence = re.sub(r"[^\w\d'\s]+", ' ', sentence)
    sentence = re.sub(r"\_", ' ', sentence)
    
    # Remove apostrophes not in the middle of words
    sentence = (' '.join(w.strip("'") for w in sentence.split()).lower())

    # Split the sentence into each word.
    pattern = re.compile(r'^\s+|\s*,\s*|\s+$|\n|\s')
    word_list = [x for x in pattern.split(sentence) if x]

    # Output needs to be a dictionary object
    # Use list comprehension (dictionary removes duplicate objects 
    # automatically)
    output = dict((i, word_list.count(i)) for i in word_list)

    return(output)

print(count_words(",\n,one,\n ,two \n 'three'"))
