def decode(string):
    
    # Set Up
    output = ''
    count = ''

    # Start Loop
    for char in string:
        if char.isdigit():
            # If it's numeric, we add it to the count string
            count += char
        else:
            if count == '':
                # this is here because this implementation of the algorithm doesn't need "1"s
                count = 1
            # Coerce the count string to integer, then repeat the character
            output += int(count) * char
            # Reset the count
            count = ''
    return output


def encode(string):
    
    # Set up
    output = ''
    count = 1
    last_char = ''

    # If null, exit gracefully
    if not string: 
        return ''

    for char in string:

        if last_char != char:
            
            # If it's a new character, add to the output, reset the counter, create new pointer
            # If the count is '1' just put in the character without the count.
            if count == 1:
                output += last_char
            else: 
                output += str(count) + last_char                

            last_char = char
            count = 1
        
        else:
            count += 1
    
    # Finish off by adding final values
    if count == 1:
        output += last_char
    else: 
        output += str(count) + last_char
    return output