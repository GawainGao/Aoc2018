
m collections import defaultdict


file = open('day12input.txt')
li = file.read().split('\n')
out = li[0].split(': ')[1].strip()
print(out)

change = {}
for line in li[2:]:
        if line:
                    change[line.split(' ')[0]] = line.split(' ')[2]

                    print(change)
                    start = 0
                    end = len(out)
                    zero_index = 0
                    for i in range(15000):
                            out = '..'+out+'..'
                                new_out = ['.' for _ in range(len(out))]
                                    read_state = '..'+out+'..'
                                        zero_index += 2
                                            start = 0
                                                end = len(new_out)-1
                                                    for j in range(len(out)):
                                                                new_out[j] = change.get(read_state[j:j+5], '.')
                                                                    while new_out[start] == '.':
                                                                                start += 1
                                                                                        zero_index -= 1
                                                                                            while new_out[end] == '.':
                                                                                                        end += - 1
                                                                                                            out = ''.join(new_out[start:end+1])
                                                                                                                print(i+1, zero_index, start, end, out)


                                                                                                                #The parttern will not change any more
                                                                                                                zero_idx = -int(50e9) + 70
                                                                                                                sumsum = 0
                                                                                                                for i in range(len(out)):
                                                                                                                        if out[i] == '#':
                                                                                                                                    sumsum += i-zero_index
                                                                                                                                            print(i-zero_index, sumsum)
                                                                                                                                            print(zero_index, len(out))
