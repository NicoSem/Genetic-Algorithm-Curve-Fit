import matplotlib.pyplot as plt
import numpy as np
import csv
import random

x = []
y = []
x2 = []
y2 = []
pop = []
size = 10
cRange = 10

def calcError(c, x, y, d):
    err = 0
    for i in range(0, len(x)):
        result = c[d]
        for j in range(0, d):
            result += c[j]*x[i]**(d-j)
        err += (y[i] - result)**2
    return err

with open('points.csv', 'r') as f:
    reader = csv.reader(f)
    line = 0
    for row in reader:
        if line != 0:
            if(row):
                #print(row)
                x.append(float(row[0]))
                y.append(float(row[1]))
        line += 1

for i in range(1,size):
    poly = [0,0,0,0]
    poly[1] = random.randint(-cRange,cRange)
    poly[2] = random.randint(-cRange,cRange)
    poly[3] = random.randint(-cRange,cRange)
    poly[0] = calcError(poly[1:4], x, y, 2)
    pop.append(poly)

for i in range(0,size-1):
    p = pop[i]

plt.scatter(x, y)
plt.show()


    