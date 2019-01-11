import collections

def input_file(fname):
    f = open(fname).read().strip().split('\n')
    return f

def read_map(l):
    a = len(l)
    b = len(l[0])
    map_list = [[' ' for i in range(a)] for _ in range(b)]
    for i in range(b):
        for j in range(a):
            map_list[i][j] = l[i][j]
    return map_list

def neibor(x,y,map):
    a = len(map)
    b = len(map[0])
    for ix in (-1, 0, 1):
        for iy in (-1, 0, 1):
            if ix == iy == 0:
                continue
            if ix + x < 0 or ix + x > a - 1 or iy + y < 0 or iy + y > b - 1:
                continue
            yield ix + x, iy + y

def problem1(lines):
    map = read_map(lines)
    a = len(map)
    b = len(map[0])

    for i in range(1000):
        new_map = [[' ' for i in range(a)] for _ in range(b)]
        for n in range(a):
            for m in range(b):
                if map[n][m] == '.':
                    if sum(map[t][k] == '|' for t, k in neibor(n, m, map)) >= 3:
                        new_map[n][m] = '|'
                    else:
                        new_map[n][m] = '.'
                elif map[n][m] == '|':
                    if sum(map[t][k] == '#' for t, k in neibor(n, m, map)) >= 3:
                        new_map[n][m] = '#'
                    else:
                        new_map[n][m] = '|'
                elif map[n][m] == '#':
                    if (sum(map[t][k] == '#' for t, k in neibor(n, m, map)) >= 1) and (sum(map[t][k] == '|' for t, k in neibor(n, m, map)) >= 1):
                        new_map[n][m] = '#'
                    else:
                        new_map[n][m] = '.'
        map = new_map.copy()
        ax, ay = count(map)
        print(i, ax*ay)
    return new_map

def count(map):
    counttree = 0
    countlumbery = 0
    a = len(map)
    b = len(map[0])
    for i in range(a):
        for j in range(b):
            if map[i][j] == '|':
                counttree += 1
            elif map[i][j] == '#':
                countlumbery += 1
    return counttree, countlumbery

def print_map(lines):
    for line in lines:
        print(line)

def main():
    l = input_file('day18.txt')
    res = problem1(l)
    a, b = count(res)
    print(a*b)
    #print(problem2(l))
    print(1000%28)
    print(1000000000%28)

if __name__ == '__main__':
    main()
