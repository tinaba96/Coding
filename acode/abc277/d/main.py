import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

if len(A) <= 1:
    print(0)
    exit()

A.sort()

for k in range(1, N):
    if A[k] - A[k-1] > 1:
        ind = k
        break

tot = sum(A)

ans = 0

A.extend(A)
#print(A)

val = 0
for i in range(1, N+N-1):
    if A[i] < A[i-1] and A[i-1] == M-1 and A[i] == 0:
        val += A[i-1]
        continue

    if A[i] < A[i-1] or A[i] - A[i-1] > 1:
        if A[i-1] != M-1 or A[i] != 0:
            val += A[i-1]
            ans = max(ans, val)
            val = 0
            #print('-----')
            continue

    #print('g: ', A[i-1])
    val += A[i-1]



#print(A)
#print(ans)
print(tot-ans)
