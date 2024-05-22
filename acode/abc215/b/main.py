import math

N = int(input())

val = int(math.log2(N))

if 2**val <= N:
    print(val)
else:
    print(val-1)


