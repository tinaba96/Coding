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


N = int(input())
S = list(input())
Q = int(input())
 

mp = [] 
two = 0
three = 0

for q in range(Q):
    t, x, c = list(map(str, input().split()))
    t = int(t)
    x = int(x)
    mp.append((t,x,c))
    if t == 1:
        S[x-1] = c
    elif t == 2:
        two = q
    else:
        three = q

flg = 'big'
p = three
if two > three:
    flg = 'small'
    p = two

if p != 0:
    if flg == 'big':
        S = [i.upper() for i in S]
    else:
        S = [i.lower() for i in S]

for i in range(p+1, Q):
    t, x, c = mp[i]
    if t == 1:
        S[x-1] = c
    

print(''.join(S))

