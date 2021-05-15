N = int(input())
tmp = 0 
tmp2 = 0 
ans = ""
anstmp = ""
A = []
for i in range(N):
    S, T = list(map(str, input().split()))
    A.append((S, T))
    if tmp < int(T):
        tmp = int(T)
for i in range(N):
    if int(A[i][1]) != tmp and int(A[i][1]) > tmp2:
        tmp2 = int(A[i][1])
        ans = A[i][0]

print(ans)

