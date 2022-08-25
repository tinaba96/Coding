# original

N, W = list(map(int, input().split()))

d = []

for i in range(N):
    w, v = list(map(int, input().split()))
    d.append((w, v))

# f(i, W) iまで判断して重さWの最大価値
'''
表
Column: 見た数
Row: 重さ
Value: 今の最大価値
'''

#mp = [[0, d[0][1]] for i in range(N)]
mp = [[0 for n in range(N)] for w in range(W+1)]

mp[d[0][0]][0] = d[0][1]

# 配るDP
for j in range(1, N):
    for k in range(W+1):
        if d[j][0]+k <= W:
            #print(mp[k+d[j][0]][j])
            mp[k+d[j][0]][j] = max(mp[k+d[j][0]][j], mp[k][j-1]+d[j][1])
        mp[k][j] = max(mp[k][j], mp[k][j-1])

#print(mp)
ans = 0

for a in range(W+1):
    ans = max(ans, mp[a][N-1])

print(ans)

