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

A = []
B = []
C = []

Ha, Wa = list(map(int, input().split()))
for i in range(Ha):
    A.append(str(input()))
Hb, Wb = list(map(int, input().split()))
for i in range(Hb):
    B.append(str(input()))
Hx, Wx = list(map(int, input().split()))
for i in range(Hx):
    X.append(str(input()))

ans = 'Yes'

for i in range(Ha):
    for j in range(Wa):
        com = []
        starti = i
        startj = j
        for p in range(Hb):
            tm = ''
            for q in range(Wb):
                if starti+p >= Ha or startj >= Wa:
                    if B[p][q] == '#':
                        tm += '#'
                    else:
                        tm += '.'
                else:
                    if A[starti+p][startj+q] == '#' or B[p][q] == '#':
                        tm += '#'
                    else:
                        tm += '.'
            com.append(tm)


        flg = True
        starti = i
        startj = j
        for ti in range(Hx):
            for tj in range(Wx):


                    




