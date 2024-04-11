import sys
sys.setrecursionlimit(2*10**5)


N =int(input())

mp = [[] for i in range(N+1)]
for n in range(N-1):
    A, B = list(map(int, input().split()))
    mp[A].append(B)
    mp[B].append(A)

for i in range(N+1):
    mp[i] = sorted(list(set(mp[i])))

ans = [1]
#print(mp)

def dfs(q, p):
    for ele in mp[q]:
        if ele == p: continue
        else:
            ans.append(ele)
            dfs(ele, q)
            ans.append(q)

dfs(1, -1) 
print(*ans)

