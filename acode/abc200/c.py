import collections
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())

A = list(map(int, input().split()))

cnt = 0
AA = [0]*N
#print(AA)

for a in range(N):
    AA[a] = A[a]%200

c = collections.Counter(AA)

# print(c)

for k,v in c.items():
    if v >= 2:
        cnt += combinations_count(v,2)


print(cnt)


