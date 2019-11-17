import re

def response(hey_bob):
    '''
    Bob the moody teenager. 
    '''
    hey_bob = hey_bob.replace(" ", "")

    # Is it an empty input?
    # This regex finds any delimited spaces at all (I think)
    if re.sub(r'\s+','',hey_bob) == "":
        return "Fine. Be that way!"

    # Is the user asking a question?
    question = False
    if hey_bob[-1] == "?":
        question = True

    # Is the user shouting?
    # Regex is to check that there are some characters present in the sentence
    shout = False
    if hey_bob.upper() == hey_bob and re.sub(r'[^A-Za-z]','',hey_bob) != "":
        shout = True

    # Responses
    if question and shout:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif shout:
        return "Whoa, chill out!"
    else:
        return "Whatever."

print(response("\t\t\t\t\t"))