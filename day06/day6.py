from collections import defaultdict

P = []
for line in open('day6.txt').readlines():
    x, y = [int(s.strip()) for s in line.split(',')]
    P.append((x,y))

print(P)
xlow = min([x for x,y in P])
xhigh = max([x for x,y in P])
ylo = min([y for x,y in P])
yhi = max([y for x,y in P])
def distan((x1,y1),(x2,y2)):
    return abs(x1-x2)+abs(y1-y2)
def close(x,y):
    ds = [(distan(p,(x,y)),p) for p in P]
    ds.sort()
    if ds[0][0] < ds[1][0]:
        return ds[0][1]
    else:
        return (-1,-1)
di = defaultdict(int)
for i in range(xlow,xhigh):
    for j in range(ylo,yhi):
        res = close(i,j)
        di[res] += 1
c = max(di,key=di.get)
print(xlow,xhigh,ylo,yhi)
ans = 0
for i in range(xlow,xhigh):
    for j in range(ylo,yhi):
        dd = 0
        for (x,y) in P:
            dd += distan((x,y),(i,j))
        if dd < 10000:
            ans += 1

print(ans)


print(di[c])
print(di)
print(max(di))
