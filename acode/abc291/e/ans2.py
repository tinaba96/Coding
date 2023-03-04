from sys import setrecursionlimit
N, M = map(int, input().split())

g = {i: set() for i in range(1, N+1)}
for _ in [0]*M:
    X, Y = map(int, input().split())
    g[X].add(Y)

seq = []
setrecursionlimit(200005)
def dfs(n):
    if length[n] != -1:
        return length[n]
    
    length[n] = 0


    for next in g[n]:
        length[n] = max(length[n], dfs(next)+1) # counting from last -> aim is to similar to ans[] in ans.py

    print(length)
    
    seq.append(n)
    return length[n]

length = [-1] * (N+1)
d = 0
for i in range(1, N+1):
    d = max(d, dfs(i))

if d == N - 1: # to check whether it reaches to end as only one possible way.
    ans = [0]*N
    print("Yes")
    seq.reverse()
    for k, i in enumerate(seq):
        ans[i-1] = k + 1
    print(*ans)
else:
    print("No")



