N = int(input())
A = list(map(int, input().split()))

import collections
import itertools
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
tot = combinations_count(N, 2)

c = collections.Counter(A)


for ele in c:
    if c[ele] >= 2:
        tot -= combinations_count(c[ele],2)

print(tot)


