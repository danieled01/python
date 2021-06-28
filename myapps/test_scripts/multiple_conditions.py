x = float(input("What's your number? "))

if x > 10:
    if type(x) == float:
        print("Greater and a Float")
elif x == 10:
    print("The Same")
else:
    print("Smaller")
