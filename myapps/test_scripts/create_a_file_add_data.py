mylist = [1,2,3]

file = "newfile.txt"
newfile = open(file, "w")

for item in mylist:
    newfile.write(str(item) + "\n")

newfile.close()
