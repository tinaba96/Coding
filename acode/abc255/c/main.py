X, A, D, N = list(map(int, input().split()))

mi = min(A, A + (N-1)*D)
ma = max(A, A + (N-1)*D)

if X <= mi:
    print(mi-X)
    exit()
if ma <= X:
    print(X-ma)
    exit()


base = X - A

diff = base % D

if diff == 0:
    print(0)
else:
    print(min(abs(diff-D), abs(diff)))



