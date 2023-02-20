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

l = len(S)
ans = ''

for i in range(l):
    #print(ord('0')^ord('1'))
    tmp = ord(S[i])^ord('0')^ord('1')
    #S[i] = ord(S[i])^ord('0')^ord('1')
    ans += chr(tmp)

print(ans)

