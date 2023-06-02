import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)
import math


N = int(input())

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

f = prime_factorization(N)

c = Counter(f)

#print(f)
ans = 0

#for i in range(1, int(math.sqrt(N))+1):
for i in range(1, N+1):
    f = prime_factorization(i)  # O(N**0.5)
    c = Counter(f)
    s = sorted(list(c))
    if len(s) != 3:
        continue

    if c[s[0]] == 2 and c[s[1]] == 1 and c[s[2]] == 2:
        ans += 1


print(ans)

# time complexity is huge
# You have to factorize all numbers less than N which is very time consuming
# total O(N*N**0.5)

