with open("day8.txt") as f:
    numbers = [int(x) for x in next(f).split()]

class Node(object):
    def __init__(self, n_childs, n_metadata):
        self.n_childs = n_childs
        self.n_metadata = n_metadata
        self.childs = []
        self.metadata = []

def sumNode(node):
    sum = 0
    for i in node.metadata:
        sum += i
    return sum

#Bulid a tree for every one
it = iter(numbers)
root = Node(next(it), next(it))
tree = []
stack = []
tree.append(root)
for _ in range(root.n_metadata):
    stack.append(("metadata", root))
for _ in range(root.n_childs):
    stack.append(("childs", root))
print(stack)
while stack:
    inst, current = stack.pop()
    if inst == "childs":
        new_node = Node(next(it), next(it))
        current.childs.append(new_node)
        if not new_node in tree:
            tree.append(new_node)
        for _ in range(new_node.n_metadata):
            stack.append(("metadata", new_node))
        for _ in range(new_node.n_childs):
            stack.append(("childs", new_node))
    else:
        current.metadata.append(next(it))

print(len(tree))
sum1 = 0
for i in tree:
    sum1 += sumNode(i)
print("New")
print(sum1)

def sumNode2(node):
    if len(node.childs) == 0:
        return sumNode(node)
    else:
        d = dict((i+1, c) for i, c in enumerate(node.childs))
        return sum(sumNode2(d.get(m, Node(0,0))) for m in node.metadata)

print(sumNode2(root))

