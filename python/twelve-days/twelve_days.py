def recite(start_verse, end_verse):

    output = []

    for i in range(start_verse, end_verse + 1):
        output.append(verse(i))

    return output

def verse(verse_number):

    # Define the gifts as a dictionary
    gifts = {
        1: " and a Partridge in a Pear Tree.",
        2: " two Turtle Doves,", 
        3: " three French Hens,",
        4: " four Calling Birds,",
        5: " five Gold Rings,",
        6: " six Geese-a-Laying,",
        7: " seven Swans-a-Swimming,",
        8: " eight Maids-a-Milking,",
        9: " nine Ladies Dancing,",
        10: " ten Lords-a-Leaping,",
        11: " eleven Pipers Piping,",
        12: " twelve Drummers Drumming,"
        }

    # Numbers
    numbers = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"    
    }

    output = "On the {} day of Christmas my true love gave to me:".format(numbers[verse_number])

    if verse_number == 1:
        output = output + " a Partridge in a Pear Tree."
        return output

    # Use a while loop
    while verse_number > 0:
        output = output + gifts[verse_number]
        verse_number += -1

    return output

print(recite(1,1))