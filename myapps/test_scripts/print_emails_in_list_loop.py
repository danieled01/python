emails=["me@gmail.com","you@hotmail.com","they@gmail.com"]

print ("Printing all emails")

for email in emails:
    print(email)

print ("Printing only gmail addresses and skipping others")

for email in emails:
    if "gmail" in email:
        print (email)
    else:
        print ("Not a gmail account skipping")
