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


N, K = list(map(int, input().split()))


ans = []
last1 = N-1
last2 = N-2

tar = 1
prevTar = -1
prevT = -1

check = []

while True:
    print('?', last1, last2, tar)
    T = int(input())
    if prevT != -1 and prevT != T:
        f = prevTar
        s = tar
        #break
        check.append(tar)
    prevT = T
    prevTar = tar
    tar += 1
    if tar == N+1:
        break

check.append(tar)
#print(f,s)
#print(check)


ans = []

v = 1
preE = 1
for e in check:
    for i in range(e-preE):
        ans.append(v)
    if v == 1:
        v = 0
    else:
        v =1
    preE = e

print('!', *ans)


'''
11 3
10001101011

のような入力の際、上記は同じ値を出力（last1, last2, tar）してしまう実装になっているが、頑張れば、
答え、または、答えが反転したやつは出力できる。
ただ、どちらが答えになるか判定できない。
K=3であれば上記の方法でできるかもだが、Kが大きい場合はうまく行かない
'''



