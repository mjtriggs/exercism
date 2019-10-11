def convert(number):
    # Initialise indicators for 3, 5, 7
    plingInd = ""
    plangInd = ""
    plongInd = ""

    # logical checks
    if (number % 3 == 0):
        plingInd = "Pling"
    if (number % 5 == 0):
        plangInd = "Plang"
    if (number % 7 == 0):
        plongInd = "Plong"

    # Return
    text = plingInd + plangInd + plongInd

    if text == "":
        return str(number)
    else: 
        return text

