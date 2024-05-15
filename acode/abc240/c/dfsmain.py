N, X = list(map(int, input().split()))

A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

box = []

def dfs(val, cnt):
    if val > X:
        return
    if X == val and cnt == N:
        print('Yes')
        exit()
    if cnt == N:
        return
    dfs(val+A[cnt], cnt+1)
    dfs(val+B[cnt], cnt+1)

dfs(0,0)
print('No')






