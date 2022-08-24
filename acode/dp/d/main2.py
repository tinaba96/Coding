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
mp = [[0 for n in range(N)] for w in range(W)]

mp[d[0][0]][0] = d[0][1]

# 配るDP
for j in range(N-1):
    for k in range(W):
        mp[d


    mp[j+1][0] = max(mp[j][0], mp[j][1])

    mp[j+1][1] = max(mp[j][0], mp[j][1]+d[j])







