# this is same as 全探索

import sys
sys.setrecursionlimit(10 ** 9)

N, K  = list(map(int, input().split()))
h  = list(map(int, input().split()))

# sから飛んで位置pに辿り着いたコスト
def f(p):
    if p == 0:
        return 0

    mi = 10**5
    for i in range(1, K+1):
        if p-i >= 0:
           mi = min(mi, abs(h[p]-h[p-i])+f(p-i))
        # mi = min(mi, abs(h[i]-h[p-i]))

    return mi

print(f(N-1))




