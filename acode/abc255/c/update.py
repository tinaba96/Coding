X, A, D, N = list(map(int, input().split()))

flag = 0

if D != 0:
    flag = (X-A)/D

if flag <= 0:
    print(abs(X-A))
    exit()
if flag >= N:
    print(abs(X-(A+D*(N-1))))
    exit()


base = X - A

diff = base % D

if diff == 0:
    print(0)
else:
    print(min(abs(diff-D), abs(diff)))



