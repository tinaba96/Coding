N, X = list(map(int, input().split()))

A = []
B = []
dif = []
mini = 0
maxi = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    mini += min(a,b)
    maxi += max(a,b)
    dif.append(maxi-mini)


if X < mini or maxi < X or X % min(dif) == 0:
    print('No')
else:
    print('Yes')








