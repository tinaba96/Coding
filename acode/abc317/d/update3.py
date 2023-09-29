from collections import deque
tot = 0
tot_x = 0
N = int(input())
need = []

for i in range(N):
    X, Y, Z = list(map(int, input().split()))
    tot += Z
    if X > Y:
        tot_x += Z
    else:
        need.append(((Y-X)//2+1, Z))

if tot_x > tot-tot_x:
    print(0)
    exit()

tot_y = tot-tot_x
dif = (tot-1)//2 + 1 - tot_x

dp = [10**6 for i in range(dif+1)]
dp[0] = 0
ans  = 10**13
l = len(need)

def dfs(q):
    global ans
    if not q:
        return

    left, ind, nd = q.popleft()

    if ind < l and smallest[ind][left] < nd: # すでにこれよりも小さい値がある場合はスキップ
        dfs(q)
        return

    ind += 1
    
    if ind == l:
        dfs(q)
        return

    d, z = need[ind]

    if smallest[ind][left] > nd:
        q.append((left, ind, nd))
        smallest[ind][left] = nd

    if left-z > 0:
        if smallest[ind][left-z] > nd+d:
            q.append((left-z, ind, nd+d))
            smallest[ind][left-z] = nd+d
    else:
        ans = min(ans, nd+d)

    dfs(q)

smallest = [[10**13 for i in range(dif+1)] for j in range(N)] # memo
q = deque([])
q.append((dif, -1, 0))
dfs(q)

print(ans)
