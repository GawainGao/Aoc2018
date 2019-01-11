from collections import *
import itertools
import random
import sys
import re

f = open("test.txt").read().strip("\n")

d = {
    "N": (0, -2),
    "E": (2, 0),
    "S": (0, 2),
    "W": (-2, 0)
}

positions = []
x, y = 10, 10
m = defaultdict(set)
prev_x, prev_y = x, y
distances = defaultdict(int)
dist = 0
for c in f[1:-1]:
    print(c, len(positions))
    if c == "(":
        positions.append((x, y))
    elif c == ")":
        x, y = positions.pop()
    elif c == "|":
        x, y = positions[-1]
    else:
        dx, dy = d[c]
        x += dx
        y += dy
        m[(x, y)].add((prev_x, prev_y))
        if distances[(x, y)] != 0:
            distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)]+1)
        else:
            distances[(x, y)] = distances[(prev_x, prev_y)]+1
        
        
    


    prev_x, prev_y = x, y
map = [['#' for i in range(20)] for j in range(20)]
print(m[12,10])
print(m)
for i in range(20):
    for j in range(20):
        if i % 2 == 1 and j % 2 == 1:
            map[i][j] = '.'


for j in range(20):
    for i in range(20):
        if m[i, j] == {(i + 2, j)}:
            map[i+1][j] = '|'
        if m[i, j] == {(i - 2, j)}:
            map[i-1][j] = '|'
        if m[i,j] == {(i, j + 2)}:
            map[i][j+1] = '-'
        if m[i,j] == {(i, j - 2)}:
            map[i][j-1] = '-'
print(map)        

finalmap = []
for i in range(20):
    s = ''
    for x in map[i]:
        s += x
    print(s)




#print(m)
print(max(distances.values()))
print(len([x for x in distances.values() if x >= 1000]))
