#needed to turn the attack string into a new string with all vowels removed

alphabet = " bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
attack = "This website is for losers LOL!"
new_attack = ""

for i in attack:
    if i in alphabet:
        new_attack += i
        
print new_attack
