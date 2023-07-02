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


Q = int(input())
S ='1'
for q in range(Q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        c = str(x[1]) # O(N)
        S += c # O(N) -> adding string will take O(N) (length of the sting) since string is the immutable that you have to create a new one  -> so this part will end up having O(Q**2)
        if len(S) > 10**10:
            i = int(S) # O(N)
            S = str(i%998244353)
    if x[0] == 2:
        S = S[1:] # this one also O(N) -> N is the length of the slice
    if x[0] == 3:
        i = int(S) #O(N)
        print(i%998244353)



