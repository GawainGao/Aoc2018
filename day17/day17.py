ZHUSHUI_X = 500
ZHUSHUI_Y = 0

def input_file(fname):
    f = open(fname).read()
    if f and f[-1] == '\n':
        f = f[:-1]
    return f.splitlines()



def read_map(l):
    map_list = []
    for line in l:
        x_or_y = line.split('=')[0]
        single = line.split('=')[1].split(',')[0]
        start = line.split('=')[2].split('..')[0]
        end = line.split('=')[2].split('..')[1]
        print(x_or_y, single, start, end)
        if line.split('=')[0] == 'x':
            for i in range(int(start), int(end) + 1):
                map_list.append((int(single), i))
        else:
            for i in range(int(start), int(end) + 1):
                #if (i, int(single)) not in map_list:
                map_list.append((i, int(single)))
    return map_list

def generate_map(maplist):
    (di, dj) = maplist[0]
    max_x, min_x = di, di
    max_y, min_y = dj, dj
    for (i, j) in maplist:
        if i > max_x:
            max_x = i
        if i < min_x:
            min_x = i
        if j > max_y:
            max_y = j
        if j < min_y:
            min_y = j
    print(max_x, min_x, max_y, min_y)
    wid = max_x - min_x + 3
    leng = max_y - min_y + 3
    map =[[' ' for _ in range(wid)] for _ in range(leng)]
    for (i, j) in maplist:
        map[j - min_y + 1][i - min_x + 1] = '#'
    map[ZHUSHUI_Y - min_y + 1][ZHUSHUI_X - min_x + 1] = ' '
    return wid, leng, min_x, min_y, map

def count_water(map):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '|' or map[i][j] == '~':
                count += 1
    return count

def problem1(lines):
    map_list = read_map(lines)    #read the input
    wid, leng, min_x, min_y, map = generate_map(map_list) #from input generate map
    h = leng - 1
    w = wid - 2
    def traverse(x, y):
        if y >= h or x < 0 or x >= w:
            return '|'
        if map[y][x] != ' ':
            return map[y][x]
        c = traverse(x, y + 1)
        if c == '|':
            map[y][x] = '|'
            print("(%d,%d) = |" % (x, y))
            return '|'

        left_open = False
        for x2 in range(x - 1, -2, -1):
            if x2 >= 0 and map[y][x2] == '#':
                break
            c = traverse(x2, y + 1)
            if c == '|':
                left_open = True
                x2 -= 1
                break
        right_open = False
        for x3 in range(x + 1, w + 1):
            if x3 < w and map[y][x3] == '#':
                break
            c = traverse(x3, y + 1)
            if c == '|':
                right_open = True
                x3 += 1
                break

        if left_open or right_open:
            result = '|'
        else:
            result = '~'
        for i in range(x2 + 1, x3):
            map[y][i] = result
        print("(%d-%d,%d) = %s" % (x2 + 1, x3, y, result))
        return result

    traverse(500 - min_x + 1, 0 - min_y)




    counts = count_water(map)     #finally count the water area
    print(map_list)
    for line in map:
        print(line)
    print(wid, leng, min_x, min_y)
    #print(count_water(map))
    return counts

def main():
    l = input_file('day17.txt')
    print(problem1(l))
    #print(problem2(l))

if __name__ == '__main__':
    main()
