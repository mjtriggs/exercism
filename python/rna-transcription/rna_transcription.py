def to_rna(dna_strand):
    '''
    Input a DNA strand and return the corresponding RNA.
    '''

    # Define dictionary - key is the DNA, value is the RNA
    rna_dict = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

    # use list comprehension to get the new string
    rna_list = [rna_dict[i] for i in dna_strand]
    
    # Convert the list to a string and output
    output = ''.join(str(elem) for elem in rna_list)
    return output