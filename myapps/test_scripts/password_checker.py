password = "hellohello"
user_name = input("What is your name? ")
user_password = input("What is your password? ")

while user_password != password:
    user_password = input("What is your password? ")

print("Well done %s you guessed it" % user_name)
