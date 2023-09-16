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
S1 = str(input())
S2 = str(input())
S3 = str(input())


ans = 100
#print(S1.index('p'))

for i in range(10):
    try:
        ind1 = S1.index(str(i))
        ind2 = S2.index(str(i))
        ind3 = S3.index(str(i))

        if ind1 == ind2:

    
        ma = max(ind1, ind2)
        ans = min(ans, max(ind3, ma))
    except:
        continue


if ans == 100:
    print(-1)
else:
    print(ans)

