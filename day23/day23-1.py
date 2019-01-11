f = open('day23.txt').readlines()

bots = []

for line in f:
    x = int(line.split('<')[1].split(',')[0])
    y = int(line.split('<')[1].split(',')[1])
    z = int(line.split('<')[1].split(',')[2].split('>')[0])
    r = int(line.split('=')[2].strip())
    bots.append((x, y, z, r))

print(bots)


def problem1(bots):
    times = 0
    max_r = 0
    max_x = bots[0][0]
    max_y = bots[0][1]
    max_z = bots[0][2]
    for bot in bots:
        if bot[3] > max_r:
            max_r = bot[3]
            max_x = bot[0]
            max_y = bot[1]
            max_z = bot[2]
    print(max_r)
    for bot in bots:
        if abs(bot[0]-max_x) + abs(bot[1]-max_y) + abs(bot[2]-max_z) <= max_r:
            times += 1
    print(times)
    return times

if __name__ == '__main__':
    problem1(bots)
