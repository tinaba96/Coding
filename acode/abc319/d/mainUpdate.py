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
    tmp += l+1

#print(cumsum)
import bisect

def ch(ind):
    #print('ind: ', ind)
    arr = cumsum
    cnt = 0
    v = ind
    while True:
        cnt += 1
        if cnt > M:
            return False
        #print('ini: ', arr)
        g = bisect.bisect_right(arr, v)
        if g == 0:
            return False
        last = arr[g-1]
        arr = arr[g:]

        if len(arr) == 0: # if arr is null, it means it is end of words -> should return True
            return True

        v = last+1
        v += ind
        #print(ind)
        #print(arr)

        
        if v > cumsum[-1]:
            cnt += 1
            #print('ans: ', cnt)
            if cnt <= M:
                return True
            else:
                return False

# mini = 24

while True: # need binary search
    if ch(mini):
        print(mini)
        exit()
    else:
        mini += 1
#print(ch(24))


