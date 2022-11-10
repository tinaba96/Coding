import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')



import itertools

N = int(input())
P = list(map(int, input().split()))

key = 0

for i in range(len(P)-1, 0 , -1):
    if P[i] < P[i-1]:
        key = i-1
        break

imp = P[key:]

new = 0 
for e in imp:
    if P[key] > e:
        new = max(new, e)

imp.remove(new)



imp.sort(reverse=True)
an = imp
#print(an)



ans = P[:key] + [new] + an

print(*ans)

