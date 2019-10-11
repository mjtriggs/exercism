def distance(strand_a, strand_b):
    # Calculate the Hamming Distance between two strands

    # Input validation
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands are not the same length.')

    # Split Strings into individual characters
    strand_a = get_characters(strand_a)
    strand_b = get_characters(strand_b)

    output = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            output += 1
    
    return output

def get_characters(word): 
    # Turns a string into a list of characters
    return [char for char in word]  
