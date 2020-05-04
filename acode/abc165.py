'''
#A
N = int(input())
A, B = list(map(int, input().split()))

vala = A//N
valb = B//N
if vala != valb or A%N == 0 or B%N == 0:
    print('OK')
elif A == B and N == 1:
    print('OK')
else:
    print('NG')

#ans
k = int(input())
a,b = map(int,input().split())
if (b//k)*k>=a:
    print('OK')
else:
    print('NG')

#B
X = int(input())
val = 100
cnt = 0
while val < X:
    val += val//100
    cnt += 1

print(cnt)

#C
from collections import defaultdict
N, M, Q = list(map(int, input().split()))
ans = 0
table = defaultdict(list)
arr = [[-1]*N for _ in range(N)]

for i in range(Q):
   a, b, c, d = list(map(int, input().split()))
   table[(a,b)] = c

for ele in table:
    if table[0]

print(ans)

#ans
N,M,Q = map(int,input().split())
abcd = [list(map(int,input().split())) for i in range(Q)]

import itertools

A = list(itertools.combinations_with_replacement(range(1,M+1),N))
answer = 0

for i in range(len(A)):
    ans = 0
    for j in range(Q):
        if A[i][ abcd[j][1]-1 ] - A[i][ abcd[j][0]-1 ] == abcd[j][2]:
            ans += abcd[j][3]
    answer = max(answer,ans)

print(answer)

#another
N, M,Q = map(int, input().split())
inf = []
for i in range(Q):
    a,b,c,d = map(int, input().split())
    inf.append([a,b,c,d])
"""深さ優先探索で数列を作る cren(r, progress,result) はrがループの回数、progressがそこまででできた数列
最後、resultに保存する　ラップ関数を定義して最後値を取り出す 再起的に呼び出す
for ループを再帰化する"""

def rap(n):#nこ長さの条件を満たす数列を作る
    result = []
    for i in range(1,M+1):
        progress = [i]
        cren(n-1,progress,result)
    return result

def cren(r,progress,result):
    if r == 0:
        result.append(progress)
        return
    a = progress[-1]
    for i in range(a,M+1):
        cren(r-1,progress+[i],result)
"""rapを呼び出すことで長さnの条件を満たす数列が帰ってくる　resultは記録用だからグローバル変数として
扱われるから成り立つ"""
ans = 0
ls = rap(N)
for item in ls:
    ani = 0
    for in1 in inf:
        a = in1[0]
        b = in1[1]
        if  (item[b-1] - item[a-1]) == in1[2]:
            ani += in1[3]
    ans = max(ans, ani)
print(ans)

#another
def solve(depth, start, stop):
    global ans
    if depth == N:
        ans = max(ans, sum(d for a, b, c, d in queries if A[b - 1] - A[a - 1] == c))
    else:
        for n in range(start, stop):
            A[depth] = n
            solve(depth + 1, n, stop)

N, M, Q = map(int, input().split())
queries = tuple(tuple(map(int, input().split())) for _ in range(Q))
A = [0] * N
ans = 0
solve(0, 1, M + 1)
print(ans)

#same as snuke
n, m, q = map(int, input().split())
abcd = []
x = [1]
ans = 0
for _ in range(q):
    abcd.append(list(map(int, input().split())))

def dfs(s):
    global ans
    if len(s) == n+1:
        now = 0
        for a, b, c, d in abcd:
            if s[b] - s[a] == c:
                now += d
        ans = max(ans, now)
        return
    p = s[-1]
    while p <= m:
        s.append(p)
        dfs(s)
        p = s.pop() + 1

dfs(x)
print(ans)
'''

#D
import math
A, B, N = list(map(int, input().split()))
ans = 0
if B+1 < N:
    C = B+1
else:
    C = N
if B//A == 0:
    D = 1
else:
    D = B//A
#floor()の中のiをD分スキップしても、全てのfloor()値を表現できる。
for i in range(1, C+D, D):
    val = math.floor(A*i/B) - A*math.floor(i/B)
    #print("i", i, "val", val)
    ans = max(ans, val)
print(ans)
#最初にエラーが出てた（testcase12)　原因は、range(1, C+1, D)とすると最後のi=Cの場合が計算されない場合があるからだった。range(1, C+D, D)とすることで解決。

import math
a,b,n=map(int,input().split())

def func(a,b,x):
    return math.floor(a*x/b)-a*math.floor(x/b)

print(func(a,b,min(b-1,n)))

'''
f (x) = f loor(Ax/B) − A × f loor(x/B) とします。
f(x + B) = f(x) であることは実際に代入することで容易に分かります。なので、0 ≤ x ≤ B − 1 の場合のみを考えます。
このとき、f (x) = f loor(Ax/B) − A × f loor(x/B) = f loor(Ax/B) で、f loor(Ax/B) は広義単 調増加なので、与えられた制約 (0 ≤ x ≤ B − 1, 0 ≤ x ≤ N) の中で最も大きい x について、f(x) が求める最大値です。
よって、答えは f (min(B − 1, N )) です。
'''
