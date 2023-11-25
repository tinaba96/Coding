N,X,Y = map(int,input().split())
A = [0] + list(map(int,input().split()))

dp_X = [dict() for _ in range(N+3)]
dp_Y = [dict() for _ in range(N+3)]

dp_X[1][0] = 1
dp_Y[1][0] = 1
dp_X[2][A[1]] = 1



L = [set() for _ in range(N+2)]
L[1].add(0)
L[2].add(A[1])

for i in range(3,N+2):
    s = L[i-2]
    if i % 2 == 0: #X
        for x in s:
            if dp_X[i-2][x] == 1:
                dp_X[i][x+A[i-1]] = 1
                dp_X[i][x-A[i-1]] = 1
                dp_X[i+1][x+A[i-1]] = 1
                dp_X[i+1][x-A[i-1]] = 1
            L[i].add(x+A[i-1])
            L[i].add(x-A[i-1])

    if i % 2 != 0: #Y
        for y in s:
            if dp_Y[i-2][y] == 1:
                dp_Y[i][y+A[i-1]] = 1
                dp_Y[i][y-A[i-1]] = 1
                dp_Y[i+1][y+A[i-1]] = 1
                dp_Y[i+1][y-A[i-1]] = 1
            L[i].add(y+A[i-1])
            L[i].add(y-A[i-1])

#print(dp_X)
#print(L[N+1])

if N%2==1:
    if X in L[N+1] and Y in L[N]:
        print("Yes")
    else:
        print("No")
else:
    if X in L[N] and Y in L[N+1]:
        print("Yes")
    else:
        print("No")




