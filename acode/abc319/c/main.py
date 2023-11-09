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


S1 = list(map(str, input().split()))
S2 = list(map(str, input().split()))
S3 = list(map(str, input().split()))

SS = S1+S2+S3
#SS = SS.extend(S3)

#print(SS)


import itertools

l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def ch(p, k, j):
    p -= 1
    k -= 1
    j -= 1
    if SS[p] == SS[k]:
        return (p, k, j)
    if SS[k] == SS[j]:
        return (k, j, p)
    if SS[j] == SS[p]:
        return (j, p, k)
    return False


loop = []

if ch(1, 2, 3):
    loop.append(ch(1, 2, 3))
if ch(4, 5, 6):
    loop.append(ch(4, 5, 6))
if ch(7, 8, 9):
    loop.append(ch(7, 8, 9))
if ch(1, 4, 7):
    loop.append(ch(1, 4, 7))
if ch(2, 5, 8):
    loop.append(ch(2, 5, 8))
if ch(3, 6, 9):
    loop.append(ch(3, 6, 9))
if ch(1, 5, 9):
    loop.append(ch(1, 5, 9))
if ch(3, 5, 7):
    loop.append(ch(3, 5, 7))

#print(loop)


cnt = 0
tot = 0
for v in itertools.permutations(l, 9):
    tot += 1
    flg = True
    for (e1, e2, e3) in loop:
        k1 = v.index(str(e1+1))
        k2 = v.index(str(e2+1))
        k3 = v.index(str(e3+1))
        if k1 < k2 < k3 or k2 < k1 <k3:
            cnt += 1
            flg = False
            break
    #if flg == False:


    #print(v)

print(1-cnt/tot)

# 計算量ギリギリ -> ローカルのでの実行は遅いが、計算量的にOK。解説動画でもローカル実行は遅く、コンパイルが最適化されていないからと言及している。ローカルのスペック等にも影響しそう。
# atcoderではpypyを実行環境（コンパイラ）として使っているが、ローカルではおそらくCPythonを使っているため、その要因もあって若干遅い。実際に、atcoderのコードテストを使用してCPythonで実行すると倍くらい実行時間が長かった。
# O(9! * 定数倍)

