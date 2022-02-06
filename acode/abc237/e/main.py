N, M  = list(map(int, input().split()))

for i in range(N):
    H  = list(map(int, input().split()))

edg = [[] for i in range(M+1)]

for i in range(M):
    print(edg)
    u, v = list(map(int, input().split()))
    edg[u].append(v)
    edg[v].append(u)
ans = 0

def dfs(now, q, joy, pas):
    global ans
    global edg
    if len(q) == 0:
        ans = max(ans, joy)
        return 
    for i in range(len(q)):
        print('a')
        pas.add(q[i])
        joy += H[q[i]] - H[now]
        for e in range(len(edg[q[i]])):
            if edg[q[i]][e] in pas:
                return
            else:
                dfs(edg[q[i]][e], edg[q[i]][e], joy)

pas = set()
print(edg[1])
dfs(1, edg[1], 0, pas)
print(ans)

#it is impposible to solve using dfs according to the video editorial
# since there are wights betwwen the node

#However, you can use it as shown in ans2.py if you dont use the video editorial approach

