import sys

n = int(sys.stdin.readline())
xy = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dict_xy = dict()
for i, (x, y) in enumerate(xy):
    dict_xy[(x, y)] = i # here, we put index to use union()

class UnionFindTree:
    def __init__(self, length):
        self.length = length
        self.parent = [i for i in range(length)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
    
    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i != parent_j:
            self.parent[parent_j] = parent_i
            return True
        else:
            return False

tree = UnionFindTree(n)
diff = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, 0], [1, 1]]
for i, (x, y) in enumerate(xy):
    for dx, dy in diff:
        if (x+dx, y+dy) in dict_xy:
            tree.union(i, dict_xy[(x+dx, y+dy)])
parents = set()
for i in range(n):
    parents.add(tree.find(i))
print(len(parents))


