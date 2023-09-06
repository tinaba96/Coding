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


N1, N2, M = list(map(int, input().split()))


mp = [[] for i in range(N1+N2+1)]

for m in range(M):
    a, b = list(map(int, input().split()))
    mp[a].append(b)
    mp[b].append(a)


#print(mp)
ans1 = 0
ans2 = 0

#dfs

visit = [False for i in range(N1+N2+1)]
def dfs(i, node):
    global ans1
    #print(visit)
    #visit = visit[:2]   # this is same ans ans. should be global
    ans1 = max(ans1, i)
    for n in node:
        if visit[n] == True:
            continue
        visit[n] = True
        #visit = [False for i in range(N1+N2+1)] # これがあるとローカル変数だとみなされ、関数内でこれより前に参照すると、定義されていないことになりエラー。
        dfs(i+1, mp[n])


def dfs2(i, node):
    global ans2
    ans2 = max(ans2, i)  # max()内のans2が関数のスコープで定義されていないため、グローバルで定義する必要がある。
    for n in node:
        if visit[n] == True:
            continue
        visit[n] = True
        dfs2(i+1, mp[n])



visit[1] = True
visit[N1+N2] = True

dfs(0, mp[1])
dfs2(0, mp[N1+N2])
#print(ans1)
#print(ans2)
print(ans1+ans2 - 1)

# ans globalにする必要ある？？ visitは？
# グローバルスコープと関数スコープの違い。visitも同様。関数内で定義されていない状態で、参照すると、同じエラー
# https://www.haya-programming.com/entry/2019/11/19/200659
# test.py

# BFS??? じゃないとダメ？ -> dfsでは距離は測れない（潜れるところまで潜るアルゴリズムのため）
# テストケース１の1,2,3の連結成分の最大パスを1->3->2と数えてしまう。本来ではあれば1->2

