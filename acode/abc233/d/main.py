N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

import collections
for k in range(N-1):
    A[k+1] += A[k]

c = collections.Counter(A)
#print(c[8])
ans = 0
for i in range(N):
    val = A[-i-1] - K
    if val == 0:
        ans += c[K]
    else:
    #print(val)
        ans += c[val]
    # delete no longer use
    # this should not be done at last since there is a case that search for same one except itself
    c[A[-i-1]] -= 1
print(ans)

