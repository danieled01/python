from prettytable import PrettyTable

def shots_per_hole(hcp,index):
    if hcp > 18 and hcp % 18 >= index:
        return 2
    elif hcp > 18 and hcp % 18 < index:
        return 1
    elif hcp == 18:
        return 1
    elif hcp < 18 and hcp % 18 <= index:
        return 1
    else:
        return 0

sf_score = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1, 2:0 }

def stableford_score(hcp,par,score,index):
    if hcp > 18 and hcp % 18 >= index:
        par = par + shots_per_hole(hcp,index)
        return 0 if (sf_score.get(score-par)) is None else (sf_score.get(score-par))
    elif hcp > 18 and hcp % 18 < index:
        par = par + shots_per_hole(hcp,index)
        return 0 if (sf_score.get(score-par)) is None else (sf_score.get(score-par))
    elif hcp == 18:
        par = par + shots_per_hole(hcp,index)
        return 0 if (sf_score.get(score-par)) is None else (sf_score.get(score-par))
    elif hcp < 18 and hcp % 18 >= index:
        par = par + shots_per_hole(hcp,index)
        return 0 if (sf_score.get(score-par)) is None else (sf_score.get(score-par))


stableford_points = 0
medal_score = 0
starting_hole = 1

hcp = int(input("What is your hcp = "))
#while hcp != int:


print("")

scorecard = PrettyTable()

scorecard.field_names = ["Hole", "Stroke Index", "Par", "Strokes", "SF Score"]


for hole in range(0,3):
    par = input("Hole {} par = ".format(starting_hole))
#    while type(par) == int:
#        par = input("I don't understand that - what is Hole {} par = ".format(starting_hole))
    score = input("Hole {} score = ".format(starting_hole))
#    while type(score) == int:
#        score = input("I don't understand that - what score did you get? ")
    index = input("Hole {} stroke index = ".format(starting_hole))
#    while type(index) == int:
#        index = input("I don't understand that - what stroke inde is Hole {}? ".format(starting_hole))
    sford_score = stableford_score(hcp,int(par),int(score),int(index))
    print("")
    stableford_points += stableford_score(hcp,int(par),int(score),int(index))
    medal_score += int(score)
    scorecard.add_row(["Hole {}".format(starting_hole), str(index), str(par), str(score), str(sford_score)])
    starting_hole += 1

scorecard.add_row(["Total Scores", "", "", str(medal_score), str(stableford_points)])

with open("scorecard.txt", "w") as myfile:
    myfile.write(str(scorecard))
print(scorecard)
