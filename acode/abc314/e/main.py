import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)

mp = []
N, M = list(map(int, input().split()))

for i in range(N):
    E = list(map(int, input().split()))
    mp.append(E)

ans = 0

def ro(m, v):
    global ans
    if m <= 0:
        ans += v
        return 0
    for i in range(N):
        c, p, *s = mp[i]
        #print(s)
        for j in range(len(s)):
            tmp = c*(s[j]/p)
            ro(m-s[j], tmp)


ro(M, 0)

print(ans)

# dp かと思ったけど、解法がよくわからない
# 上記の方法は再帰潜りすぎかと思われる。 O(P^N)
# どのルーレットを選ぶのが最適かO(PN)で求め、DPしていく（またはメモ化再帰）ことで、O(MNP)で求めることができる。
# 再帰はans3.py

# dp[x]:  残りのx点の状態からの期待値
# xの小さい順に求めていくことで、効率よく計算できる



