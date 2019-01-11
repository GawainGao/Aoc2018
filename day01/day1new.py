with open('day1.txt') as f:
    data = [int(x) for x in f.readlines()]
print(sum(data))
import itertools
freq = 0
seen = {0}
for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq)
        break
    seen.add(freq)
