H, W = list(map(int, input().split()))
Q = int(input())
ma = [[0 for i in range(W)] for j in range(H)]
box = set()

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ma[q[1]][q[2]] = 1
    else:
        if ma[q[1]][q[2]] == 1 and ma[q[3]][q[4]] == 1:
            print('Yes')
        else:
            print('No')

        




