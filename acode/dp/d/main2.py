N, W = list(map(int, input().split()))

d = {}

for i in range(N):
    w, v = list(map(int, input().split()))
    d[w] = v

# f(i, W) iまで判断して重さWの最大価値
'''
表
Column: 見た数
Row: 重さ、もしくは0、1
Value: 今の最大価値
'''

mp = [[0,0] for i in range(N)]

for j in range(N-1):
    mp[j+1][0] = max(mp[j][0], mp[j][1]+d[])
    mp[j+1][1] = max(mp[j][0], mp[j][1]+)







