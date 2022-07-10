import math
N = int(input())
count = 0

for i in range(1, N+1):
    d = 2
    k = i
    while d*d <= k:
        while k%(d*d) == 0:
            k /= d*d
        d += 1
    d = 1
    while k*d*d <= N:
        count += 1
        d += 1

print(count)
