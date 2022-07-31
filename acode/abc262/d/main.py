N = int(input())
a = list(map(int, input().split()))

mod = 998244353

ans = N

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


import math
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(1,N+1):
    #print(prime_factorize(a[i-1]))
    cnt = 0
    for j in range(N):
        if a[j]%i == 0:
            cnt += 1
    if i > 1 and cnt >= i:
        ans += combinations_count(cnt, i)
        #print(ans)
print(ans)


