INF=1000 # if you filp 1000 times, which means you filip all rows, 0 and 1 will be swapped and, isolate element still be isolated
f=lambda:map(int,input().split())
h,w=f()
A=[[*f()] for _ in range(h)]
dp=[[0,1],[0,1]] # whether it is flip or not for last 2 rows, for this case, only the 1st row is flipped or not
for i in range(1,h):
  dpn=[[INF,INF],[INF,INF]]
  for j in range(2):
    for k in range(2):
      nj=k
      for nk in range(2):
        X=[-1]*w # if edge
        if i>1: X=[a^j for a in A[i-2]] # j is whether it will flip or not
        Y=[a^k for a in A[i-1]] # k is whether it will flip or not
        #Y=[a^nj for a in A[i-1]]
        Z=[a^nk for a in A[i]] # nk is whether it will flip or not
        ok=1
        # check Y
        for c in range(w):
          if X[c]!=Y[c]!=Z[c] and (c==0 or Y[c]!=Y[c-1]) and (c==w-1 or Y[c]!=Y[c+1]):
            ok=0
        if i==h-1: # check last row of Z
          for c in range(w):
            if Z[c]!=Y[c] and (c==0 or Z[c]!=Z[c-1]) and (c==w-1 or Z[c]!=Z[c+1]):
              ok=0
        if ok:
          dpn[nj][nk]=min(dpn[nj][nk],dp[j][k]+nk)
  dp=dpn
ans=min(min(dp[j][k] for k in range(2)) for j in range(2))
print([-1,ans][ans<INF])


# see the video tutorial

'''
import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

H, W = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(H)]

dp = [[float("inf")] * 3 for _ in range(3)]

dp[2][2] = 0

for i in range(H):
    tmp = [[float("inf")] * 3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            for z in range(2):  # 現在の状態
                # この状態が成り立つかのチェック
                f = True
                if x == 2 or i == 0:
                    pass
                else:
                    for k in range(W):
                        f2 = False
                        if A[i - 1][k] ^ x == A[i][k] ^ z:
                            f2 = True
                        if k > 0:
                            if A[i - 1][k] ^ x == A[i - 1][k - 1] ^ x:
                                f2 = True
                        if k < W - 1:
                            if A[i - 1][k] ^ x == A[i - 1][k + 1] ^ x:
                                f2 = True
                        if i > 1:
                            if A[i - 1][k] ^ x == A[i - 2][k] ^ y:
                                f2 = True
                        if not f2:
                            f = False
                            break

                if f:
                    tmp[z][x] = min(tmp[z][x], dp[x][y] + z)

    dp = tmp

ans = float("inf")

i = H - 1
for x in range(3):
    for y in range(3):
        f = True
        for k in range(W):
            f2 = False
            if k > 0:
                if A[i][k] ^ x == A[i][k - 1] ^ x:
                    f2 = True
            if k < W - 1:
                if A[i][k] ^ x == A[i][k + 1] ^ x:
                    f2 = True
            if A[i][k] ^ x == A[i - 1][k] ^ y:
                f2 = True
            if not f2:
                f = False
                break
        if f:
            ans = min(ans, dp[x][y])

if ans == float("inf"):
    print(-1)
else:
    print(ans)
'''


