import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data_file = "data.json"
open_imported_data = open(data_file)
imported_data = json.loads(open_imported_data.read())

def check_word(word):
    word = word.lower()
    if word in imported_data.keys():
        return imported_data[word]
    elif word.title() in imported_data.keys():
        return imported_data[word.title()]
    elif word.upper() in imported_data.keys():
        return imported_data[word.upper()]
    elif len(get_close_matches(word,imported_data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y if yes and N if no: " %get_close_matches(word,imported_data.keys())[0])
        if yn == "Y":
            return imported_data[get_close_matches(word,imported_data.keys())[0]]
        elif yn == "N":
            return "That word doesnt exist please check your entry"
        else:
            return "We didnt understand your instructions please try again."
    else:
        return "Sorry I don't understand that word"

user_word = input("Please enter your word? ")

output = (check_word(user_word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
