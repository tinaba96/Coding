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


mp = []
N = int(input())
for n in range(N):
    s = str(input())
    mp.append(s)
    

def ch(t):
    #print(t)
    flg = True
    for i in range(len(t)//2):
        if t[i] != t[-i-1]:
            flg = False
    return flg


ans = 'No'

for q in range(N):
    for j in range(N):
        if q == j:
            continue
        if ch(mp[q]+mp[j]):
            ans = 'Yes'

print(ans)




