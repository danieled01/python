string = int(input("Please enter you text here: "))

def length(user_input):
    if type(user_input) == float:
        print("Sorry floats don't have length")
    elif type(user_input) == int:
        print("Sorry ints don't have length")
    else:
#        return len(user_input)
        print("The word you have entered is", len(user_input), "characters long")

length(string)
