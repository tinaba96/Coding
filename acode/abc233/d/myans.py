N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

import collections
for k in range(N-1):
    A[k+1] += A[k]

A.insert(0,0)
c = collections.Counter(A)
#c[0] += 1
#print(c)
#print(c[8])
ans = 0
for i in range(N):
    c[A[-i-1]] -= 1
    val = A[-i-1] - K
    ans += c[val]

print(ans)

