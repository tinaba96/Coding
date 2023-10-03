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

#print(cumsum)
import bisect

def ch(ind):
    cnt = 1
    v = ind

    for ele in L:  # O(N)

        if ind < ele: # this is needed and important
            return False

        if v-ele < 0:
            v = ind # initialize
            cnt += 1
            if cnt > M:
                return False
        elif v-ele != 0:
            v -= 1
        v -= ele

    return True

while True: # this should be binary search (size of Li is 10^9 so we need binary seach) -> 10^9 * 2*10^5 = 2*10^14 at maximum
    if ch(mini):
        print(mini)
        exit()
    else:
        mini += 1
    
# O(N*logN)
# this code is still TLE -> need to use binary search

