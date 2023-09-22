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


N, M = list(map(int, input().split()))
L = list(map(int, input().split()))

# dp
#print(sum(L))
mini = sum(L)//M
#print(mini)

cumsum = []
tmp = 0
for l in L:
    cumsum.append(tmp+l)
    tmp += l

#print(cumsum)
import bisect

def ch(ind):
    cnt = 1
    v = ind


    for ele in L:
        if v-ele < 0:
            v = ind
            cnt += 1
            if cnt > M:
                return False
        elif v-ele != 0:
            v -= 1
        v -= ele


    return True

while True: # binary search? (size of Li is 10^9 so we need binary seach but why WA?)
    if ch(mini):
        print(mini)
        exit()
    else:
        mini += 1
    

# O(N*logN)
