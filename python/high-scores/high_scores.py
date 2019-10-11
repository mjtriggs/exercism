def latest(scores):
    # Return the last value in the list (i.e. the latest score)
    return scores[-1]


def personal_best(scores):
    # Just take the maximum
    return max(scores)


def personal_top_three(scores):
    output = scores
    
    # Sort the list from largest to smallest then output the first three entries
    output.sort(reverse = True)
    return output[0:3]