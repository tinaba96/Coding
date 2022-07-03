X, A, D, N = list(map(int, input().split()))

# you need this because you are comparing with the value to take care of minus version and plus version. However, if you consider index like the video tutorial, you don't need to compare like this
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



