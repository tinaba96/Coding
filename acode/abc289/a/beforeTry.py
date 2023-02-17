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


S = int(input(), 2)
l = len(str(S))

#print(bin(S | 10**2))
#print(bin(2**7-1))
#print(S)
ans = bin(S ^ 2**11-1)




#print(format(~x & 0b1111, '04b'))
#print(ans)
print(ans[len(ans)-l:])

# or: 1 | 1 = 1 -> it will not reverse 
