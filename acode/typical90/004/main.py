H, W = list(map(int, input().split()))

m = [[0 for i in range(W)] for j in range(H)]


for h in range(H):
    A = list(map(int, input().split()))
    for a in range(W):
        m[h][a] = A[a]




