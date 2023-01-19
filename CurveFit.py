import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

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

plt.scatter(x, y)
plt.show()