import matplotlib.pyplot as plt
import numpy as np
import csv
import random

x = []
y = []
y2 = []
p = []
size = 10
cRange = 10
iterations = 10

def calcError(c, x, y, d):
    err = 0
    for i in range(0, len(x)):
        result = c[d]
        for j in range(0, d):
            result += c[j]*x[i]**(d-j)
        err += (y[i] - result)**2
    return err

def calcValues(c, x, d):
    err = 0
    for i in range(0, len(x)):
        result = c[d]
        for j in range(0, d):
            result += c[j]*x[i]**(d-j)
        y2.append(result)
    return y2

def rank(r):
    #print("a" + str(len(r)))
    
    for i in range(0,len(r)-1):
        s = len(r)
        a = r.pop(i)
        #print(a)
        for j in range(0,len(r)-1):
            if a[0] < p[j][0]:
                r.insert(j, a)
                break
        if len(r) < s:
            r.append(a)
    #print("b" + str(len(r)))
    return r

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



for i in range(0,size):
    poly = [0,0,0,0]
    poly[1] = random.randint(-cRange,cRange)
    poly[2] = random.randint(-cRange,cRange)
    poly[3] = random.randint(-cRange,cRange)
    poly[0] = calcError(poly[1:4], x, y, 2)
    
    p.append(poly)

p = rank(p)

for i in range(1, iterations):
    c1 = [0,0,0,0]
    c1[1] = (p[0][1] + p[1][1]) / 2
    c1[2] = (p[0][2] + p[1][2]) / 2
    c1[3] = (p[0][3] + p[1][3]) / 2
    c1[0] = calcError(c1[1:4], x, y, 2)

    c2 = [0,0,0,0]
    c2[1] = (p[2][1] + p[3][1]) / 2
    c2[2] = (p[2][2] + p[3][2]) / 2
    c2[3] = (p[2][3] + p[3][3]) / 2
    c2[0] = calcError(c2[1:4], x, y, 2)

    p.append(c1)
    p.append(c2)

    p = rank(p)

    p.pop(len(p)-1)
    p.pop(len(p)-1)

print(p)

plt.figure(1)
plt.scatter(x, y)

plt.figure(1)
plt.plot(x, calcValues(p[0][1:4], x, 2), color='red')
plt.show()


    