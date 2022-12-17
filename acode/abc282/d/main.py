import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')



'''
2部グラフの判定を行うプログラム

N := 頂点の数
M := 辺の数

A,B　:= 頂点Aから頂点Bにかけて無向の辺があることを示す

dict := 辺のつながりを格納する
　　　　 collections の　dict　だとValueに配列を格納しやすい

color　:= 頂点が何色で塗られているか

'''

#print(color)

from collections import deque
from collections import defaultdict

N,M = list(map(int,input().split()))
G = defaultdict(set)

color = [0 for i in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    G[A].add(B)
    G[B].add(A)

color[1] = 1
que = deque(["1"])#始点を追加
bipartite = True

def sol(c, q, bi):

    while len(que):
        p = q.popleft()#直近で追加したグラフの頂点を取得
        p = int(p)
        for qa in list(G[p]):#結合しているグラフの頂点を参照
            qa = int(qa)
            #print(type(q))
            if c[qa] == 0:#塗られていないなら別の色で塗る
                c[qa] = -c[p]
                q.append(str(qa))
            elif c[qa] == c[p]:#同じ色だったら2部グラフではないと返し終了させる
                bi = False
                break
sol(color, que, bipartite)
print(color)

for i in range(len(color)):
    if color[i] == 0:
        print('yes')
        sol(color, deque([str(i)]), bipartite)

print(color)
cntn = 0
cntp = 0

'''
flg = True
for g in range(len(color)):
    if color[i] != 0:
        flg = False
if flg:
    print(0)
    exit()
print(color)
'''


#print(color)
#print(ans)
