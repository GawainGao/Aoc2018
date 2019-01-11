from collections import defaultdict
data = [line for line in open('day4.txt').readlines()]
data.sort()
print(data)

def readData(data):
    words = data.split()
    date = words[0][1:]
    time = words[1][:-1]
    guards = words[3][1:]
    return guards, int(time.split(':')[1])

C = defaultdict(int)
CM = defaultdict(lambda: defaultdict(int))
CMI = defaultdict(int)
guard = None
asleep = None
for line in data:
    if line:
        _, time = readData(line)
        if 'begins' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls' in line:
            asleep = time
        elif 'wakes' in line:
            print((asleep, time))
            for t in range(asleep, time):
                CM[guard][t] += 1
                C[guard] += 1
                CMI[guard] += time - asleep

print(CM)
print(C)
print(CMI)
def argmax(l):
    best = None
    for k,v in l.items():
        if best is None or v > l[best]:
            best = k
    return best

best_guard = argmax(C)
print(argmax(C))
print(argmax(CM[best_guard]))
print(argmax(C)*argmax(CM[best_guard]))
