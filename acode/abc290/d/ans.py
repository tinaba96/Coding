import math

t = int(input())

for i in range(t):
    n,d,k = map(int,input().split())
    gcd = math.gcd(n,d) # n, d の差が3と言うイメージ。3ずつずれていくイメージ。(50と35の場合、gcdの5ずつずれていくのがわかる)
    c = n//gcd　# gcd(3) ずつずれていくので、全体nをgcdで割った商4が最初に戻ってくるまでの周期と言える。
    cc = (k-1)//c # それを何周するか。それが最終的に被った回数。
    print((d*(k-1)+cc)%n)


# we don't need to think of "int b" in video editorial
# "int i = k/m" where it represents how many times it is collided is the most important part here.





'''
from math import gcd
import sys
sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9 + 7
def input(): return sys.stdin.readline().rstrip()
def Yes(b): return bool([print('Yes')] if b else print('No'))
def YES(b): return bool([print('YES')] if b else print('NO'))


def int1(x): return int(x) - 1


T = int(input())
for _ in range(T):
    N, D, K = map(int, input().split())
    D %= N
    g = gcd(N, D)
    a = N // g
    p, q = divmod(K - 1, a)
    ans = p + q * D
    ans %= N
    print(ans)

'''


