score = [3,7]
input = 890691
equallist = [8,9,0,6,9,1]
a = 0
b = 1
i = 0
while True:
    add = score[a] + score[b]
    if add >= 10:
        ten = add % 10
        one = add // 10
        score.append(one)
        score.append(ten)
    else:
        score.append(add)
    #print(score)
    a += score[a] + 1
    a %= len(score)
    b += score[b] + 1
    b %= len(score)
    #i += 1
    #if i > 6:
        #print("Check",score[-6:])
    if score[-6:] == equallist or score[-7:-1] == equallist:
        break

print(len(score) - 6)
print(len(score) - 7)
#print(*score[input:input+10],sep="")


