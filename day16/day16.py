import difflib
from collections import Counter

lines = open('day16.txt').read().split('\n')
#print(lines)



before = []
after = []
operate = []
for i in range(len(lines)):
    if i % 4 == 0:
        before.append(lines[i])
    if i % 4 == 2:
        after.append(lines[i])
    if i % 4 == 1:
        operate.append(lines[i][-7:])
print(before)
print(after)
print(operate)
'''
def compare(str1, str2):
    for i in [9,12,15,18]:
        #print(str1[i], str2[i])
        if str1[i] != str2[i]:
            position = (i - 9) // 3
            return (position, str1[i], str2[i])

print(compare(before[0],after[0]))
'''
def addr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) + register_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def addi(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) + op_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def mulr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) * register_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def muli(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) * op_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def banr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) & register_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def bani(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) & op_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def borr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) | register_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def bori(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po]) | op_value
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def setr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(be[be_po])
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def seti(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value = int(op[4])
    register_value = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    res = int(op[2])
    #print(be,op,af,opcode,op_value,register_value,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def gtir(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value_a = int(op[2])
    op_value_b = int(op[4])
    register_value_a = int(be[int(op[2]) * 3 + 9])
    register_value_b = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    if op_value_a > register_value_b:
        res = 1
    else:
        res = 0
    #print(be,op,af,opcode,op_value_a,register_value_b,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def gtri(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value_a = int(op[2])
    op_value_b = int(op[4])
    register_value_a = int(be[int(op[2]) * 3 + 9])
    register_value_b = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    if register_value_a > op_value_b:
        res = 1
    else:
        res = 0
    #print(be,op,af,opcode,op_value_a,register_value_b,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def gtrr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value_a = int(op[2])
    op_value_b = int(op[4])
    register_value_a = int(be[int(op[2]) * 3 + 9])
    register_value_b = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    if register_value_a > register_value_b:
        res = 1
    else:
        res = 0
    #print(be,op,af,opcode,op_value_a,register_value_b,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def eqir(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value_a = int(op[2])
    op_value_b = int(op[4])
    register_value_a = int(be[int(op[2]) * 3 + 9])
    register_value_b = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    if op_value_a == register_value_b:
        res = 1
    else:
        res = 0
    #print(be,op,af,opcode,op_value_a,register_value_b,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def eqri(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value_a = int(op[2])
    op_value_b = int(op[4])
    register_value_a = int(be[int(op[2]) * 3 + 9])
    register_value_b = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    if register_value_a == op_value_b:
        res = 1
    else:
        res = 0
    #print(be,op,af,opcode,op_value_a,register_value_b,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def eqrr(be,op,af):
    opcode = op[0]
    be_po = int(op[2]) * 3 + 9
    op_value_a = int(op[2])
    op_value_b = int(op[4])
    register_value_a = int(be[int(op[2]) * 3 + 9])
    register_value_b = int(be[int(op[4]) * 3 + 9])
    af_po = int(op[6]) * 3 + 9
    if register_value_a == register_value_b:
        res = 1
    else:
        res = 0
    #print(be,op,af,opcode,op_value_a,register_value_b,be[be_po],af[af_po],res)
    if res == int(af[af_po]):
        return 1
    else:
        return 0

def problem1(be, op, af):
    return addr(be, op, af) \
    + addi(be, op, af) \
    + mulr(be, op, af) \
    + muli(be, op, af) \
    + setr(be, op, af) \
    + seti(be, op, af) \
    + banr(be, op, af) \
    + bani(be, op, af) \
    + borr(be, op, af) \
    + bori(be, op, af) \
    + gtir(be, op, af) \
    + gtri(be, op, af) \
    + gtrr(be, op, af) \
    + eqri(be, op, af) \
    + eqir(be, op, af) \
    + eqrr(be, op, af)

res = [[] for i in range(16)]
print(res)
OPERATION = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
def problem2(be, op, af):
    for operation in OPERATION:
        op_res = operation(be, op, af)
        if op_res == 1:
            pos = op.split(' ')
            res[int(op[0])].append(operation.__name__)
            print(op[0])
            print(operation.__name__)

count = 0
'''
for i in range(len(before)):
    if problem1(before[i],operate[i],after[i]) >= 3:
        count += 1
    print("count: ", count)
'''
for i in range(len(before)):
    print(i)
    problem2(before[i], operate[i], after[i])
#for i in range(16):
#    print(res[i])
unique_ops = {}
for i in range(10):
    m, n = Counter(res[i]).most_common(1)[0]
    print("Number", i, "is", m)
    unique_ops[i] = m

print(unique_ops)

initial = [0, 0, 0, 0]
#Because it needs to return the result, so the function should be changed
print(res)

'''
print(problem1(before[0],operate[0],after[0]))
print("addr: ",addr(before[0],operate[0],after[0]))
print("addi: ",addi(before[0],operate[0],after[0]))
print("mulr: ",mulr(before[0],operate[0],after[0]))
print("muli: ",muli(before[0],operate[0],after[0]))
print("setr: ",setr(before[0],operate[0],after[0]))
print("seti: ",seti(before[0],operate[0],after[0]))
print("banr: ",banr(before[0],operate[0],after[0]))
print("bani: ",bani(before[0],operate[0],after[0]))
print("borr: ",borr(before[0],operate[0],after[0]))
print("bori: ",bori(before[0],operate[0],after[0]))
print("gtir: ",gtir(before[0],operate[0],after[0]))
print("gtri: ",gtri(before[0],operate[0],after[0]))
print("gtrr: ",gtrr(before[0],operate[0],after[0]))
print("eqir: ",eqir(before[0],operate[0],after[0]))
print("eqri: ",eqri(before[0],operate[0],after[0]))
print("eqrr: ",eqrr(before[0],operate[0],after[0]))
'''
