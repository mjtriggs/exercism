import numpy as np
import re

def is_valid(isbn):
    '''
    Function to check if candidate ISBN is valid.
    '''

    # Remove all punctuation from isbn and turn into a list
    isbn = re.sub(r'[^A-z0-9]', "", isbn)
    input_list = [char for char in isbn]

    # If there are not 10 valid digits, then fail the test
    if len(list(filter(re.compile("[X0-9]").match, input_list))) != 10:
        return False

    # Replace any value of X with 10
    for (i, value) in enumerate(input_list):
        if value == "X" and i != 9:
            # X is only valid as the check (final) digit. False if anywhere else.
            return False
        elif value == "X":
            input_list[i] = 10
        else:
            input_list[i] = int(value)

    # Set corresponding vector for multiplication and use np.dot to calculate a test value
    scalar_list = list(range(1, 11))[::-1]
    check_sum = np.dot(scalar_list, input_list) % 11

    # If the value is 0 mod 11, then it is valid
    return bool(check_sum == 0)
    