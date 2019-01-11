from collections import defaultdict, deque

E = defaultdict(list)
D = defaultdict(int)

for line in open('day7.txt'):
    words = line.split()
    x = words[1]
    y = words[7]
    E[x].append(y)
    D[y] += 1

for k in E:
    E[k] = sorted(E[k])
ans = ""
for x in E:
    print(x, E[x])
Q = deque()
for y in E:
    if D[y] == 0:
        Q.append(y)
print(Q)
'''
ans = ""
while Q:
    x = sorted(Q)[0]
    Q = [y for y in Q if y!=x]
    ans += x
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            Q.append(y)
'''
print(ans)
#time
t = 0
EV = []
QU = []
def add_task(x):
    QU.append(x)
def start_work():
    global QU
    while len(EV) < 5 and QU:
        print(QU)
        x = min(QU)
        QU = [y for y in QU if y!= x]
        print('Starting ', x , ' at ', t)
        EV.append((t+61+ord(x)-ord('A'), x))
        print(EV)

for k in E:
    if D[k] == 0:
        add_task(k)
print(QU)
start_work()
while EV or QU:
    (t, x) = min(EV)
    print("Check: ",t,x)
    EV = [y for y in EV if y!=(t,x)]
    for y in E[x]:
        D[y] -= 1
        if D[y] == 0:
            add_task(y)
    start_work()

print(t)



t = 0
EV = []
Q = []

def add_task(x):
    Q.append(x)


