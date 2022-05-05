N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
D = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    D[x][y] = 1
    D[y][x] = 1


def popcount(x):
    x = (x & 0x5555555555555555) + (x >> 1 & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2 & 0x3333333333333333)
    # this is also OK
    #x = (x & 0x0f0f0f0f0f0f0f0f) + (x >> 4 & 0x0f0f0f0f0f0f0f0f)
    x = x + (x >> 4) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7f

INF = 10**18
dp = [[INF] * (1 << N) for _ in range(N)]
for i in range(N):
    dp[i][1 << i] = A[i][0]

#thi is also ok
# for s in range(1, 6):
for s in range(1, 1 << N):
    #print(bin(s))
    k = popcount(s)
    # k ewpewsent how many people have been set already. if all of them are one (full), it means that all people are set and no more person will be set
    for j in range(N):
        if s & (1 << j): continue
        # consider all possible people
        for i, Di in enumerate(D):
            if Di[j]: continue
            # s|(1<<j) is a sction to pin(mark) the person in j index. this binary represents a person who is set. if it is all "1", it means the all the perple has been set already.
            dp[j][s | (1 << j)] = min(dp[j][s | (1 << j)], dp[i][s] + A[j][k])
            # dp[i][s] search for previous status. otherwise INF

ans = min(dp[i][(1 << N) - 1] for i in range(N))
print(ans if ans < INF else -1)

# for popcount please refer this
# https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266

'''
def popcount(x):
   #xの立っているビット数をカウントする関数
   # (xは64bit整数)

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f
'''
