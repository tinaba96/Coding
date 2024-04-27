import sys
sys.setrecursionlimit(10**6)
def dfs(v):
    # 連結成分でなければ返す
    if not flag[v]:
        return
    flag[v] = False
    for nx in g[v]:
        dfs(nx)

n = int(input())
a = list(map(int, input().split()))
res = 0

# i番目が連結成分の対象になっているかどうか
flag = [False] * 2000005
for nx in a:
    if not flag[nx]:
        flag[nx] = True
        # A に含まれる整数の種類数
        res += 1

# 連結成分
# Ai と An+1-i番目を無向グラフでつなぐ
g = [[] for _ in range(200005)]
for i in range(n // 2):
    g[a[i]].append(a[n - 1 - i])
    g[a[n - 1 - i]].append(a[i])

for i in range(1, 200000+1):
    # i番目のフラグが立っていれば、連結成分なので連結を外す
    if flag[i]:
        res -= 1
        dfs(i)
print(res)


