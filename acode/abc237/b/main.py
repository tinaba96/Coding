H, W = list(map(int, input().split()))

A = []
B = []

for h in range(H):
    a = list(map(int, input().split()))
    A.append(a)


for w in range(W):
    tmp = []
    for h in range(H):
        tmp.append(str(A[h][w]))
    B.append(tmp)

for w in range(W):
    print(' '.join(B[w]))





