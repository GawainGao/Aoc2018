import re
import numpy as np
with open('day3.txt') as f:
    num = []
    for line in f.readlines():
        r = re.split('[^0-9]+',line[1:].strip())
        num.append([int(d) for d in r])
fabric = np.zeros((1000,1000))
def part1():
    for n,x,y,le,wi in num:
        fabric[x:x+le,y:y+wi] += 1
    return np.sum(fabric > 1)

def part2():
    for n,x,y,le,wi in num:
        if np.all(fabric[x:x+le,y:y+wi] == 1):
            return n

print(part1())
print(part2())
