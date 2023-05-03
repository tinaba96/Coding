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


ans = -1
cnt = 0

ind = 0 
flg = False
while True:
    if S[ind] == '-':
        flg = True
        if cnt > 0:
            ans = max(ans, cnt)
        cnt = 0
    if S[ind] == 'o' and flg == True:
        cnt += 1
    ind += 1
    if ind == N:
        if flg == True and cnt > 0:
            ans = max(ans, cnt)

        break


S = S[::-1]

#print(S)

cnt = 0
ind = 0
flg = False

while True:
    if S[ind] == '-':
        flg = True
        if cnt > 0:
            ans = max(ans, cnt)
        cnt = 0
    if S[ind] == 'o' and flg == True:
        cnt += 1
    ind += 1
    if ind == N:
        if flg == True and cnt > 0:
            ans = max(ans, cnt)
        break


print(ans)

