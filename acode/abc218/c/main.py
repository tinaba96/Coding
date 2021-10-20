N = int(input())

ma = [["." for i in range(N)] for j in range(N)]
#print(ma)
for i in range(N):
    S = str(input())
    for s in range(N):
        if S[s] == "#":
            ma[i][s] = "#"
    
comp = [["." for i in range(N)] for j in range(N)]
for i in range(N):
    T = str(input())
    for t in range(N):
        if T[t] == "#":
            comp[i][t] = "#"


tmp1 = [["." for i in range(N)] for j in range(N)]
tmp2 = [["." for i in range(N)] for j in range(N)]
tmp3 = [["." for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        tmp1[i][j] = ma[N-1-j][i]

for i in range(N):
    for j in range(N):
        tmp2[i][j] = ma[j][N-i-1]

for i in range(N):
    for j in range(N):
        tmp3[i][j] = ma[N-i-1][N-j-1]
#print(ma)
#print(tmp3)

def check(A, B):
    ind = []
    ind2 = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == "#":
                ind.append((i, j))
            if B[i][j] == "#":
                ind2.append((i, j))
    if len(ind) != len(ind2):
        return False
    a = ind[0][0]-ind2[0][0]
    b = ind[0][1]-ind2[0][1]
    flag = True
    for p in range(len(ind)):
        if a != ind[p][0]-ind2[p][0] or b != ind[p][1]-ind2[p][1]:
            flag = False

    if flag:
        return True
    else:
        return False

if check(comp, ma) or check(comp, tmp1) or check(comp, tmp2) or check(comp, tmp3):
    print('Yes')
else:
    print('No')
