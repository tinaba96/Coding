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

import copy


N, K = list(map(int, input().split()))
oA = list(map(int, input().split()))

Q = int(input())

for i in range(Q):
    A = oA.copy()
    l, r = list(map(int, input().split()))
    leng = r-l+1
    for p in range(leng-1): #Q
        target = A[p+l-1] - A[p+l]
        if p+l-1+K-1 >= r:
            break
        for g in range(K):
            if p+l+g-1 == r:
                break
            A[p+l+g-1] += target

    #print(A)
    flg = True
    base = A[l-1]
    print(A)
    for c in range(leng):
        if A[l+c-1]-base != 0:
            print('No')
            flg = False
            break

    if flg:
        print('Yes')






    








