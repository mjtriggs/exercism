class Luhn(object):
    def __init__(self, card_num):

        # store the raw input 
        self.raw_input = card_num

    def valid(self):
        
        # Initial input validation
        clean_input = self.raw_input.replace(" ", "")
        if len(clean_input) == 1:
            return False

        # Check everything is a digit
        if clean_input.isdigit() == False:
            return False

        # Turn into a list for list comprehension
        input_as_list = [int(char) for char in clean_input]

        # Reverse the list to make the next part easier
        input_as_list.reverse()

        # Luhn Algorithm - Double every second value
        # Luhn's Algorithm looks from the right, but we've reverse the list so go from the left
        input_as_list[1::2] = [doubling_function(i) for i in input_as_list[1::2]]
        
        # Valid numbers are equal to 0 mod 10.
        total = sum(input_as_list)
        if total % 10 == 0:
            return True
        else: 
            return False

def doubling_function(x):
    if x*2 <= 9:
        return x*2
    else: 
        return x*2 - 9
