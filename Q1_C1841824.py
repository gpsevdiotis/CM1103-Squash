import random
import math
import csv
import matplotlib.pyplot as plt

#1a
def game(ra,rb):
    p = ra/(ra+rb)
    scores = [0,0]
    a = False
    while a == False:
        r = random.random()
        if r < p:
            scores[0] += 1
        else:
            scores[1] += 1
        if (scores[0] >= 11 or scores [1] >= 11) and math.fabs(scores[0]-scores[1]) >= 2 :
            a = True
            return scores

#1b
def winProbability(ra, rb, n):
    PlayerAwins = 0
    PlayerBwins = 0
    for i in range(0,n):
        g = game(ra,rb)
        if g[0] > g[1]:
            PlayerAwins += 1
        else:
            PlayerBwins += 1
    Probability = PlayerAwins / n
    return round(Probability, 2)

#1c
def reader(name):
    x = []
    y = 0
    with open(name) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if y >=1:
                x.append((row[0],row[1]))
            y += 1
    return x


#1d
def wins(list):
    x = []
    y = []
    for tuples in list:
        y.append(winProbability(int(tuples[0]),int(tuples[1]),10000))
        x.append(int(tuples[0])/int(tuples[1]))
    x,y = zip(*sorted(zip(x,y)))
    plt.plot(x,y, 'b', label = 'PARS')
    plt.title("Probability Player A beats player B \n against ra / rb ")
    plt.ylabel("Probability player A wins")
    plt.xlabel("ra / rb")
    plt.yticks ([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
    plt.xticks ([0,0.5,1,1.5,2,2.5,3])
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()


#1e
def simulation():
    wp = winProbability(60,40, 100000)
    if wp > 0.9:
        return 1
    else:
        for n in range (0,100):
            prob = 0
            for g in range(0, (2 * n - 2)):
                if g == 0:
                    prob += (wp ** n) * ((1 - wp) ** (g))
                else:
                    prob += (wp ** n) * ((1 - wp) ** (g)) * (math.factorial(n) / (math.factorial(n-1) * math.factorial(n - (n - 1))))
            if prob >= 0.9:
                return n


print(game(70,30))
print(winProbability(70,30,10000))
print(reader("test.csv"))
wins(reader("test.csv"))
print(simulation())
