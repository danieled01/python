cel = float(input("Celsius to be converted "))  #global variable

def cels_to_farh(cel):                          #cel here is a local varable to the function
    farh = cel * 9/5 + 32                       #far and cel local variables
    return farh

if cel >= -273.15:
    print ((cels_to_farh(cel))
else:
    print ("That's far too cold")
