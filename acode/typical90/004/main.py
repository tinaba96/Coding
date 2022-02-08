H, W = list(map(int, input().split()))

m = [[0 for i in range(W)] for j in range(H)]
ans = [[0 for i in range(W)] for j in range(H)]


for h in range(H):
    A = list(map(int, input().split()))
    for a in range(W):
        m[h][a] = A[a]

#print(m)
warr = [] 
harr = [] 
for k in range(H):
    harr.append(sum(m[k]))

#print(warr[0])

for p in range(W):
    tmp = 0
    for q in range(H):
        tmp += m[q][p]
    warr.append(tmp)

#print(harr[0])

for i in range(H):
    for j in range(W):
        ans[i][j] = harr[i] + warr[j] - m[i][j]


for i in range(H):
    tmp = [str(a) for a in ans[i]]
    print(" ".join(tmp))
#print(' '.join(ans[0]))





