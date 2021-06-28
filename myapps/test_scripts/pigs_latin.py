def pig_latin(txt):
    vowels = ["a", "e", "i", "o", "u"]
    if txt[0] in vowels and txt[0] == txt[0].upper():
        return txt.title() + "way"
    elif txt[0] in vowels:
        return txt + "way"
    elif txt[0] == txt[0].upper():
        return txt[1:].title() + txt.lower()[0] + "ay"
    elif txt[-1] == ".":
        return txt[1:-1] + txt.lower()[0] + "ay" + txt[-1]
    else:
        return txt[1:] + txt.lower()[0] + "ay"

list1 = ["Cats", "are", "great", "pets."]
list2 = ["Tom", "got", "a", "small", "piece", "of", "pie."]
list3 = ["He", "told", "us", "a", "very", "exciting", "tale."]


for item in list1:
    print(pig_latin(item))
print("")
for item in list2:
    print(pig_latin(item))
print("")
for item in list3:
    print(pig_latin(item))
