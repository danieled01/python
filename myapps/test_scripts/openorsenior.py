#Script to work out if open or senior


results = [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
x=0
y=1
myresults = []

def openorsenior(age,hcp):
    if age >= 55 and hcp > 7:
       myresults.append ("Senior")
    else:
       myresults.append ("Open")


for i in range(len(results)):
    openorsenior(results[x][0],results[x][1])
    x += 1

print myresults
