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


p, q = list(map(str, input().split()))

list = 'ABCDEFG'

v = [3, 1, 4, 1, 5, 9]
 # index() check!!!!

s = 0
e = 0
for i in range(7):
    if list[i] == p:
        s = i
    if list[i] == q:
        e = i


ans = 0
for a in range(min(s,e), max(s, e)):
    #print(a)
    ans += v[a]

print(ans)



