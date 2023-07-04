import sys
sys.setrecursionlimit(500005)
import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
pypyjit.set_param('max_unroll_recursion=-1')



'''
2部グラフの判定を行うプログラム

N := 頂点の数
M := 辺の数

A,B　:= 頂点Aから頂点Bにかけて無向の辺があることを示す

dict := 辺のつながりを格納する
　　　　 collections の　dict　だとValueに配列を格納しやすい

color　:= 頂点が何色で塗られているか

'''

from collections import defaultdict 

N,M = map(int,input().split())
dict = defaultdict(set)

for i in range(M):
    a,b = list(map(int,input().split()))  

    dict[a].add(b)
    dict[b].add(a)

ans = 0

color = [0 for i in range(N+1)]
res = 'Yes'

def dfs(v,c,queue=[]):
    u'''
    v : 現在のグラフの頂点
    c : 現在参照するフラグ,1=>-1=>1と使うので渡す必要がある
    queue : 探索したグラフの頂点を入れていく
    res : global変数を使いたくないが,再帰のreturnがよくわからないのでとりあえず
    '''

    global color
    global res 
    queue.append(v)

    for i in list(dict[v]):
        if color[i] == c:#隣の頂点が同じ値を与えられている際Falseを返す
            res = 'No'
        elif i not in queue:#探索済みでなければ再帰する
            color[i] = c*-1#0ならcとは異なる値を格納
            dfs(i,-c,queue)#引数に-cとすることで,cが1=>-1=>1を繰り返す


color[1] = 1#始点色分けする
(dfs(1,1))
#print(color)

cntn = 0
cntp = 0

for i in range(1, len(color)):
    if color[i] == 0:
        color[i] = 1
        dfs(i, 1)
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

if res == "No":
    print(0)
    exit()

for i in range(len(color)):
    if color[i] == -1:
        cntn += 1
    elif color[i] == 1:
        cntp += 1

for i in range(len(color)):
    if color[i] == -1:
        cnt = len(dict[i])
        ans += cntp - cnt
#print(color)
print(ans)


