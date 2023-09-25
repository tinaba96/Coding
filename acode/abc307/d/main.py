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
S = str(input())



ind = []
cnt = 0
ind2 = []

imp = []
imp2 = ()

left = 0

mag = set()
list = set()

for i in range(N):
    if S[i] == '(':
        ind.append(i)
    elif S[i] == ')':
        ind2.append(i)
        if len(ind) != 0:
            left = ind.pop()
            imp.append((left, i)) 

    else:
        mag.add(i)

    
for a, b in imp: # this is TLE  O(N^2)
    #print(a, b)
    for i in range(a, b+1):
        list.add(i)

#print(list)
ans = ''
for k in range(len(S)):
    if k in list:
        continue
    else:
        ans += S[k]

print(ans)

