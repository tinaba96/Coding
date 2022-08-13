A = []
B = []

ch = []

H, W = list(map(int, input().split()))

for i in range(H):
    I = list(map(int, input().split()))
    A.append(I)

check = []

H2, W2 = list(map(int, input().split()))
for j in range(H2):
    J = list(map(int, input().split()))
    ch.append((i, J[0]))
    B.append(J)



if H < H2 or W < W2:
    print('No')
    exit()

first = [] 

for i in range(H):
    for j in range(W):
        if B[0][0] == A[i][j]:
            first.append((i, j))

for ele in first:
    h = ele[0]
    w = ele[1]

    for k in range(H2-1):
        for ee in range(ele[1], W):
            if A[h][ee] == B[k][w]:





