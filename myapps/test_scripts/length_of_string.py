to_be_calculated = 5


def calc_length(str_to_be_calc):
    length = len(str_to_be_calc)
    return  length

if type(to_be_calculated) == str:
    print ("The length of the string is " + str(calc_length(to_be_calculated)) + " characters")
elif type(to_be_calculated) == float:
    print ("The length of this can't be calculated as it is a float")
else:
    print ("You can't calculate the length of this data object")
