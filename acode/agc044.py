#A
'''
T = int(input())

for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
    ans = 0

    def coins(val, coin):
        if val == N:
            if coin < ans:
                ans = coin
                print(ans)
                return 
        elif val > N:
            val = 1
            coin = D
            return
        else:
            coins(val+1, coin+D)
            coins(val*2, coin+A)
            coins(val*3, coin+B)
            coins(val*5, coin+C)
            coins(val-1, coin+D)

    coins(0, 0)
    print(ans)

'''

T = int(input())

for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
    val = N

    def coins(val, a, b, c, d, ans):
        if val%2 != 0 and val%3 != 0 and val%5 != 0:
            d += 1
            val -= 1
        elif val%2 == 0:
            val /= 2
            a += 1
        elif val%3 == 0:
            val /= 3
            b += 1
        elif val%5 == 0:
            val /= 5
            c += 1
        print(a,b,c,d)


        if val == 0:
            ans = min(ans, A*a+B*b+C*c+D*d)

            return ans
        else:
            coins(val, a, b, c, d, ans)

    print(coins(val, 0, 0, 0, 0, 0))

            



'''
T = int(input())


for i in range(T):
    N, A, B, C, D = list(map(int, input().split()))
    ans = 1001001001
    val = 0

    for a in range(N//2+1):
        for b in range(N//3+1):
            for c in range(N//5+1):
                tmp = 2**a*3**b*5**c 
                d = abs(N - tmp)
                ans = min(ans, a*A+b*B+c*C+(d+1)*D)
                #print(ans)

    print(ans)

#ans
t = int(input())

def solve(n,a,b,c,d):
  mem = {0:0,1:d}
  def f(n):
    if n in mem:
      return mem[n]
    ret = n*d
    if n%2 == 0:
      ret = min(ret,a+f(n//2))
    else:
      ret = min(ret,a+d+f(n//2+1),a+d+f(n//2))

    if n%3 == 0:
      ret = min(ret,b+f(n//3))
    elif n%3 == 1:
      ret = min(ret,b+d+f(n//3))
    else:
      ret = min(ret,b+d+f(n//3+1))

    if n%5 == 0:
      ret = min(ret,c+f(n//5))
    elif n%5 == 1:
      ret = min(ret,c+d+f(n//5))
    elif n%5 == 2:
      ret = min(ret,c+d+d+f(n//5))
    elif n%5 == 3:
      ret = min(ret,c+d+d+f(n//5+1))
    else:
      ret = min(ret,c+d+f(n//5+1))
    mem[n] = ret
    return ret
  return f(n)

for _ in range(t):
  n,a,b,c,d = map(int,input().split())
  print(solve(n,a,b,c,d))

                   


#B
N = int(input())
P = list(map(int, input().split()))

'''


#Bans→理解できていない
import sys
import numpy as np
from numba import njit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit('(i4,i4[::1])', cache=True)
def solve(N, P):
    W = N + 2
    dp = np.zeros((W, W), np.int32)
    for _ in range(4):
        dp = dp.T[::-1]
        for n in range(1, (N + 1) // 2 + 1):
            dp[n, n:-n] = n
    filled = np.zeros_like(dp)
    filled[1:-1, 1:-1] = 1
    dp = dp.ravel()
    filled = filled.ravel()
    stack = np.empty_like(dp)
    ans = 0
    for n in P:
        n -= 1
        h, w = divmod(n, N)
        v = (h + 1) * W + (w + 1)
        ans += dp[v] - 1
        filled[v] = 0
        k = min(dp[v - 1], dp[v + 1], dp[v - W], dp[v + W])
        if dp[v] == k:
            return ans
        p = 0
        stack[0] = v
        dp[v] = k
        while p >= 0:
            v = stack[p]
            p -= 1
            for dx in (-1, 1, -W, W):
                w = v + dx
                k = dp[v] + filled[w]
                if dp[w] > k:
                    dp[w] = k
                    p += 1
                    stack[p] = w
    return ans

N = int(readline())
P = np.array(read().split(), np.int32)

print(solve(N, P))

#C++
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 500 + 3;
int H[MAXN][MAXN];
bool occ[MAXN][MAXN]; #席が空いているかどうか
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void dfs(int x, int y) {
    int z = H[x][y] + occ[x][y];
    for (int t = 0; t < 4; t++) {
        int x1 = x + dx[t], y1 = y + dy[t];
        if (H[x1][y1] > z) {
            H[x1][y1] = z; #影響を受ける席を更新
            dfs(x1, y1);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    #各席における最短距離をHに保持させる。各席に最短距離を割り当てる。
    for (int i = 1; i <= N; i++) for (int j = 1; j <= N; j++) {
        H[i][j] = min(min(i, N+1-i), min(j, N+1-j)) - 1; #縦か横か近い方
        occ[i][j] = true; #席が埋まる
    }

    int res = 0;
    for (int it = 0; it < N*N; it++) {
        int id;
        cin >> id;
        int x = (id+N-1)/N; #行番号
        int y = id % N; #列番号
        if (y == 0) y += N;
        res += H[x][y];
        occ[x][y] = false; #席が空く
        dfs(x, y);
    }
    cout << res << "\n";

}



#C

