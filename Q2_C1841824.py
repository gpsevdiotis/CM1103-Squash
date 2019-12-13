import random
import math
import csv
import matplotlib.pyplot as plt

def gamePARS(ra, rb):
    p = ra/(ra+rb)
    scores = [0,0]
    rally = 0
    a = False
    while a == False:
        r=random.random()
        if r<p:
            scores[0]=scores[0]+1
        else:
            scores[1]=scores[1]+1
        rally+=1
        if (scores[0]>=11 or scores[1]>=11) and math.fabs(scores[0]-scores[1])>=2:
            a=True
            return scores,rally

def gameENGLISH(ra, rb):
    p = ra/(ra+rb)
    server = random.choice([1,2])
    scores = [0,0]
    rally = 0
    a = False
    victory = 9
    while a == False:
        r = random.random()
        if r < p and server == 1:
            scores[0]=scores[0]+1
        elif r < p and server == 2:
            server = 1
        elif r >= p and server == 2:
            scores[1]=scores[1]+1
        elif r >= p and server == 1:
            server = 2
        if scores[0] == 8 and scores[1] == 8:
            victory = random.choice([9,10])
        rally += 1
        if scores[0] == victory or scores[1] == victory:
            a = True
            return scores,rally

def winProbabilityPARS(ra,rb,n):
    ProbAWins = 0
    rally = 0
    for i in range(0,n):
        g = gamePARS(ra,rb)
        if g[0][0] > g[0][1]:
            ProbAWins += 1
        rally += g[1]
    probability = ProbAWins / n
    average_rally = rally / n
    return round(probability, 2), average_rally

def winProbabilityENGLISH(ra,rb,n):
    ProbAWins = 0
    rally = 0
    for i in range(0,n):
        g = gameENGLISH(ra,rb)
        if g[0][0] > g[0][1]:
            ProbAWins += 1
        rally += g[1]
    probability = ProbAWins / n
    average_rally = rally / n
    return round(probability,2),average_rally

def reader(name):
    x = []
    y = 0
    with open(name) as csvfile:
        read = csv.reader(csvfile)
        for row in read:
            if y >=1:
                x.append((row[0],row[1]))
            y += 1
    return x

def AwinsGraph(list):
    x = []
    y = []
    x1 = []
    y1 = []
    for tuples in list:
        x.append(int(tuples[0])/int(tuples[1]))
        y.append(winProbabilityPARS(int(tuples[0]),int(tuples[1]),10000)[0])
        x1.append(int(tuples[0])/int(tuples[1]))
        y1.append(winProbabilityENGLISH(int(tuples[0]),int(tuples[1]),10000)[0])
    x,y=zip(*sorted(zip(x,y)))
    x1,y1=zip(*sorted(zip(x1,y1)))
    plt.title("PARS VS English Scoring \n Probability A wins over B")
    plt.ylabel("Probality player A wins")
    plt.xlabel("ra/rb")
    plt.plot(x,y,"b", label = "PARS")
    plt.plot(x1,y1,"r", label = "English")
    plt.legend(loc= "upper left")
    plt.yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.grid()
    plt.show()

def rally(list):
    x = []
    y = []
    x1 = []
    y1 = []
    for tuples in list:
        x.append(int(tuples[0])/int(tuples[1]))
        y.append(winProbabilityPARS(int(tuples[0]),int(tuples[1]),10000)[1])
        x1.append(int(tuples[0])/int(tuples[1]))
        y1.append(winProbabilityENGLISH(int(tuples[0]),int(tuples[1]),10000)[1])
    x,y=zip(*sorted(zip(x,y)))
    x1,y1=zip(*sorted(zip(x1,y1)))
    plt.title("Pars VS English Scoring \n Difference in Rallies per Game")
    plt.ylabel("Number of Rallies per Game")
    plt.xlabel("ra/rb")
    plt.plot(x,y,"b", label = "PARS")
    plt.plot(x1,y1,"r", label = "English")
    plt.legend(loc= "upper right")
    plt.yticks([10,12,14,16,18,20,22,24,26,28])
    plt.xticks([0,10,20,30,40,50,60,70,80])
    plt.grid()
    plt.show()

AwinsGraph(reader("test2.csv"))
rally(reader("test3.csv"))
