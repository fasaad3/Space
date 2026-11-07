from math import *

file = open("27_B_21932.txt")

clust1 = []
clust2 = []
clust3 = []

for line in file:
    line = line.replace(',', '.')
    x, y = map(float, line.split())
    if y < 10: clust1.append((x, y))
    elif x > 17: clust2.append((x, y))
    else: clust3.append((x, y))

mi = float(inf)
center1 = 0
center2 = 0
center3 = 0
for star in clust1:
    dst = sum([dist(star, i) for i in clust1])
    if dst < mi:
        mi = dst
        center1 = star
mi = float(inf)
for star in clust2:
    dst = sum([dist(star, i) for i in clust2])
    if dst < mi:
        mi = dst
        center2 = star
mi = float(inf)
for star in clust3:
    dst = sum([dist(star, i) for i in clust3])
    if dst < mi:
        mi = dst
        center3 = star

print(center3[0] * 10000, center1[1] * 10000)