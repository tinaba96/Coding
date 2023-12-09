import sys
sys.setrecursionlimit(5000050)
import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
pypyjit.set_param('max_unroll_recursion=-1')

# A = list(map(int, input().split()))
N, x, y = list(map(int, input().split()))
A = list(map(int, input().split()))

a = A[0]
b = 0

# from
# left 1
# down 2
# right 3 # top 4

from collections import defaultdict
d = defaultdict(bool)

#d[(3, 5)] = 3
#print(d)
#print(d[(3, 5)])

def check(r, v, ind, di):
    #print(r, v)
    if ind == N and r == x and v == y:
        print('Yes')
        exit()
    if ind == N:
        return True
    else:
        if di == 1 or di == 3:
            if d[(r,v+A[ind], ind)] == False:
                d[(r,v+A[ind], ind)] = check(r, v+A[ind], ind+1, 2)

            if d[(r,v-A[ind], ind)] == False:
                d[(r, v-A[ind], ind)] = check(r, v-A[ind], ind+1, 4)

        elif di == 2 or di == 4:
            if d[(r+A[ind], v, ind)] == False:
                d[(r+A[ind], v, ind)] = check(r+A[ind], v, ind+1, 1)

            if d[(r-A[ind], v, ind)] == False:
                d[(r-A[ind], v, ind)] = check(r-A[ind], v, ind+1, 3)
    return True


check(a, b, 1, 1)


print('No')

