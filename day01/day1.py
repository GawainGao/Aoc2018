s = {0}
sum = 0
with open('day1.txt') as f:
    for line in f.readlines():
        if line[0] == '+':
            sum += int(line[1:])
            if sum in s:
                print(sum)
                break
            else:
                s.add(sum)
        else:
            sum -= int(line[1:])
            if sum in s:
                print(sum)
                break
            else:
                s.add(sum)
print("Total:",sum)
