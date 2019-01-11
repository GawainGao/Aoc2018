from collections import Counter
with open('day2.txt') as f:
    data = [line for line in f.readlines()]
c = [0, 0]
for line in data:
    a = [j for (_, j) in Counter(line).most_common()]
    if 2 in a:
        c[0] += 1
    if 3 in a:
        c[1] += 1
print(c[0]*c[1])
for i in data:
    for j in data:
        diffs = 0
        for idx, ch in enumerate(i):
            if ch != j[idx]:
                diffs += 1
        if diffs == 1:
            ans = [ch for (idx,ch) in enumerate(i) if ch == j[idx]]
print(''.join(ans))
