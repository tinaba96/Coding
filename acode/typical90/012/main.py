H, W = list(map(int, input().split()))
Q = int(input())
ma = [[0 for i in range(W+1)] for j in range(H+1)]
box = set()

class UF:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[Fjx] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [self.leader(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n): result[leader_buf[i]].append(i)
        return [r for r in result if r != []]


for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ma[q[1]][q[2]] = 1
        box.add((q[1], q[2]))
        print(box)
    else:
        if ma[q[1]][q[2]] == 1 and ma[q[3]][q[4]] == 1:
            print('Yes')
        else:
            print('No')

        




