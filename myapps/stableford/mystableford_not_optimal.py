def stableford_points(hcp,par,index,score):
    sf_score = { -4:6, -3:5, -2:4, -1:3, 0:2, 1:1, 2:0 }
    diff = score - par
    if hcp > 18 and index <= hcp % 18 and diff == -4:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -4:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -3:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -3:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -2:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -2:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == -1:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == -1:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 0:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 0:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 1:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 1:
        return ((sf_score.get(diff)) + 1)
    elif hcp > 18 and index <= hcp % 18 and diff == 2:
        return ((sf_score.get(diff)) + 2)
    elif hcp > 18 and index >= hcp % 18 and diff == 2:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -4:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -3:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -2:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == -1:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 0:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 1:
        return ((sf_score.get(diff)) + 1)
    elif hcp == 18 and diff == 2:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index <= hcp % 18 and diff == -4:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -4:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -3:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -3:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -2:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -2:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == -1:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == -1:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 0:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 0:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 1:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 1:
        return ((sf_score.get(diff)))
    elif hcp < 18 and index <= hcp % 18 and diff == 2:
        return ((sf_score.get(diff)) + 1)
    elif hcp < 18 and index > hcp % 18 and diff == 2:
        return ((sf_score.get(diff)))
    else:
        return 0

stableford_score = 0

hcp = int(input("What is your hcp = "))


for hole in range(0,2):
    par = int(input("Hole par = "))
    score = int(input("Hole score = "))
    index = int(input("Hole stroke index = "))
    stableford_score += stableford_points(hcp,par,index,score)


print("Your stableford score is", stableford_score)
