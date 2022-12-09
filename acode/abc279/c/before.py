from collections import defaultdict
dox = defaultdict(int)

S = []
T = []

H, W = list(map(int, input().split()))

for i in range(H):
    s = str(input())
    S.append(s)
for j in range(H):
    t = str(input())
    T.append(t)

for a in range(W):
    tmp = ''
    for b in range(H):
        tmp += S[b][a]
    dox[tmp] += 1

for e in range(W):
    tmp2 = ''
    for z in range(H):
        tmp2 += T[z][e]
    dox[tmp2] -= 1
    if dox[tmp2] < 0:
        print('No')
        exit()
print('Yes')


