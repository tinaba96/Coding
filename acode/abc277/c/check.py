import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

a = []
b = []
mp = {}

from collections import defaultdict
d = defaultdict(list)


N = int(input())
mx = 0

for i in range(N):
    A, B = list(map(int, input().split()))
    mx = max(max(mx, A),B)
    d[A].append(B)
    d[B].append(A)

ans = 1
memo = defaultdict(int)
#memo = dict()
#print(memo[2])
past = set()

def lad(st):
    ne = d[st]
    '''
    if len(ne) == 0:
        return st
    '''
    mos = st
    for e in ne:
        if e in past:
            continue
        else:
            past.add(e)
        '''
        if memo[e] != 0:
            mos = memo[e]
        else:
            mos = max(mos, lad(e))
        '''
        mos = max(mos, lad(e))
    #memo[st] = mos
    return mos


print(lad(ans))

#print(d[mx])

