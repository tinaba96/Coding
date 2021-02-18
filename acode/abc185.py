#practicing

'''
#C
import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

L = int(input())

print(comb(L-1, 11))
'''

#D
import math
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

if (M == 0):
    print(1)
    exit()

A.sort() 

if N-A[-1] != 0 and A[0]-1 != 0:
    k = min(N-A[-1], A[0]-1)
elif N-A[-1] == 0 and A[0]-1 != 0:
    k = A[0]-1
elif N-A[-1] != 0 and A[0]-1 == 0:
    k = N-A[-1]
else:
    k = N

for i in range(0,M-1):
    tmp = A[i+1]-A[i]-1
    if k > tmp and tmp != 0:
        k = tmp

ans = 0
ans += math.ceil((A[0]-1)/k)
ans += math.ceil((N-A[-1])/k)

for i in range(M-1):
    ans += math.ceil(((A[i+1]-A[i])-1)/k)

print(ans)






