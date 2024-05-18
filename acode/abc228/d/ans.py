N = 1 << 20
Q = int(input())
A = [-1] * N
P = [-1] * (N + 1)


def root(x):
    if P[x] < 0:
        return x
    P[x] = root(P[x])
    return P[x]


def union(x, y):
    y = root(y)
    P[x] = y # next index


for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x % N
        target = root(h)
        if target == N:
            target = root(0)
        A[target] = x
        union(target, target + 1)
    if t == 2:
        print(A[x % N])


