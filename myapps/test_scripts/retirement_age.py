retirement_age_uk = 67
retirement_age_it = 65
retirement_age_fr = 60

age = float(input("How old are you? "))
location = input("Where do you live? (uk,it,fr) ")

def uk_ret(age):
    years_left = 67 - age
    return years_left

def it_ret(age):
    years_left = 65 - age
    return years_left

def fr_ret(age):
    years_left = 60 - age
    return years_left

if age <= 67 and location == "uk":
    print ("You have " + str(uk_ret(age)) + " left to work in the UK")
elif age <= 65 and location == "it":
    print ("You have " + str(it_ret(age)) + " left to work in Italy")
elif age <= 60 and location == "fr":
    print ("You have " + str(fr_ret(age)) + " left to work in France")
else:
    print ("You should have retired")
