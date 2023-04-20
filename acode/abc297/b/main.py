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

ans = 'No'

flg = True
b = -1
r = []

for i in range(len(S)):
    if S[i] == 'B':
        if b == -1:
            b = i%2
        else:
            if b == i%2:
                flg = False
    if S[i] == 'R':
        r.append(str(i))
    if S[i] == 'K':
        t = i

if int(r[0]) > t or int(r[1]) < t:
    flg = False

if flg == True:
    ans = 'Yes'

print(ans)






