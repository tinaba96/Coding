import collections


N = int(input())
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

g = 0
n = N
if N % 2 != 0:
    n = N-1

while n > 2:
    n /= 2
    g += 1

        
cnt = collections.Counter(prime_factorize(N))


print(cnt)

arr = []
ans = 0

for k in cnt:
    if cnt[k] >= 2:
        arr.append(cnt[k]-1)

for e in arr:
    ans += e
#print('a', min(arr))
ans += min(arr)
#print(N-g)
print(ans)


