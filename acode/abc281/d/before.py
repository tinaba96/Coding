import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, K, D = list(map(int, input().split()))
a = list(map(int, input().split()))

da = []

for i in range(N):
    if a[i]%D == 0:
        da.append(a[i])

da = sorted(da, reverse=True)

#print(da)
    
print(sum(da[:K]) if sum(da[:K]) != 0 else -1)
