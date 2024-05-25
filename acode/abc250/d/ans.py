import math

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
ans = 0

tmp = N // 2 + 1
tmp = math.pow(tmp,1/3)

li = primes(int(tmp))

for q in li:
  for p in li:
    if p >= q:
      break
    if p*q**3 > N:
      break
    ans += 1

print(ans)
