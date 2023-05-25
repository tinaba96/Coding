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


S = str(input())
T = str(input())

masterS = 0
masterT = 0

for i in range(len(S)):
    if S[i] == '@':
        masterS += 1
    if T[i] == '@':
        masterT += 1


master = 'atcoder@'
master = set(list(master))

S = list(S)
T = list(T)

c = Counter(T)
#print(c)

for s in S:
    #print('s :', s)
    if s == '@':
        continue
    if c[s] > 0:
        c[s] -= 1
    elif c['@'] > 0 and s in master:
        c['@'] -= 1
    else:
        print('No')
        exit()

for j in c:
    if c[j] > 0:
        if j not in master:
            print('No')
            exit()

print('Yes')
#print(c['a'])

