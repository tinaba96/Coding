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
T = str(input())


for i in range(N):
    if S[i] != T[i]:
        if S[i] == '1' and T[i] == 'l':
            continue
        if T[i] == '1' and S[i] == 'l':
            continue
        if S[i] == 'o' and T[i] == '0':
            continue
        if T[i] == 'o' and S[i] == '0':
            continue
    if S[i] == T[i]:
        continue
    print('No')
    exit()


print('Yes')


# normalization is effective (see the video editorial)



