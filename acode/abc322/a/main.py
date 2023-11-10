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


n = int(input())
N = str(input())

N = list(N)
#print(N)

for i in range(len(N)-2):
    if N[i] == 'A' and N[i+1] == 'B' and N[i+2] == 'C':
        print(i+1)
        exit()

print(-1)




