import math
N = int(input())

qmax = 10**6
'''
def prime(N):
  primes = []
  for i in range(2, N + 1):
    primes.append(i)
    for p in range(2, i):
      if i % p == 0:
        primes.remove(i)
        break
  return primes
'''

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime

pr = []

prime = sieve_of_eratosthenes(10**6)
for p in range(10**6+1):
    if prime[p]:
        pr.append(p)

        #print(p, end=' ')
#print(pr)
#print(len(pr))
#print(sum(prime(10**6)))
#print(pr)
anss = set()


for p in range(len(pr)):
    for q in range(p+1, len(pr)):
        if pr[q] <= pr[p]:
            break
        v = pr[q]**3
        if pr[p]*v not in anss:
            anss.add(p*v)

print(len(anss))        





