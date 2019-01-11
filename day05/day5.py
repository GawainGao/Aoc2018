alpha = 'abcdefghijklmnopqrstuvwxyz'
M = {}
for c in alpha:
    M[c.lower()] = c.upper()
    M[c.upper()] = c.lower()

with open('day5.txt') as f:
    s = f.read().strip()
ans = 111111
for rm in alpha:
    s2 = [c for c in s if c!=rm.lower() and c !=rm.upper()]
    stack = []
    for c in s2:
        if stack and c==M[stack[-1]]:
            stack.pop()
        else:
            stack.append(c)
    ans = min(ans, len(stack))

print(ans)



