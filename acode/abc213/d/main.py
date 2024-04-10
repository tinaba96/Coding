N =int(input())
mp = [[] for i in range(N+1)]
for n in range(N-1):
    A, B = list(map(int, input().split()))
    mp[A].append(B)
    mp[B].append(A)

for i in range(N):
    mp[i] = list(set(mp[i]))

ans = [1]
#print(mp)

def dfs(ans, q, used):
    if len(q) == 0:
        return
    tmp=q.pop()
    for ele in mp[tmp]:
        if used[ele] == 0:
            used[ele] = 1
            ans.append(ele)
            q.append(ele)
            dfs(ans, q, used)
            ans.append(ele)
        else:
            continue


used = [0 for i in range(N+1)]
 
for i in range(N+1):
    used[i] = 0

used[1] = 1
dfs(ans,[1], used) 
print(*ans)

