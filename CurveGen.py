import matplotlib.pyplot as plt
import numpy as np
import csv
import random

x = []
y = []

yMin = -10
yMax = 10
points = 21
degree = 2
noise = 10

f = open('points.csv', 'w')
writer = csv.DictWriter(f, fieldnames=['x', 'y'])
writer.writeheader()

for i in np.arange(yMin, yMax, (yMax - yMin)/points):
    result = (i**2 - noise + 2*noise*random.uniform(0,1))
    y.append(i)
    x.append(result)
    writer.writerow({'x': str(i), 'y': result})

plt.scatter(y, x)
plt.show()