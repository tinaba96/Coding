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


H, W = list(map(int, input().split()))

A = []
B = []

for h in range(H):
    #a = list(map(str, input().split()))
    a = str(input())
    A.append(a)


for h in range(H):
    #b = list(map(str, input().split()))
    b = str(input())
    B.append(b)

if A == B:
    print('Yes')
    exit()

'''
for w in range(W+10):
    for hh in range(H):
        #print('bef', A[hh])
        t = list(A[hh])
        ts = ''.join(t[1:])+t[0]
        A[hh] = ts

        #print('aft', A[hh])
        if A == B:
            print('Yes')
'''


for h in range(H+10):
    #print(A)
    #print(A[1])
    tmp = A[1:]
    tmp.append(A[0])
    A = tmp
    #print('a', A)
    #for hh in range(H):
    if A == B:
        print('Yes')
        exit()

    for w in range(W+10):
        for hh in range(H):
            #print('bef', A[hh])
            t = list(A[hh])
            ts = ''.join(t[1:])+t[0]
            A[hh] = ts

            #print('aft', A[hh])
        if A == B:
            print('Yes')
            exit()
print('No')




