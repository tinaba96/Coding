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

#prime = sieve_of_eratosthenes(10**6)
#for p in range(10**6+1):
t = int(N**(1/3))
prime = sieve_of_eratosthenes(int(t)+1)
for p in range(t+1):
    if prime[p]:
        pr.append(p)

        #print(p, end=' ')
#print(pr)
#print(len(pr))
#print(sum(prime(10**6)))
#print(pr)
anss = set()

cnt = 0

test = []

#print(pr[0])

# this is O(n^2) which leads to TLE
for p in range(len(pr)):
    for q in range(p+1, len(pr)): # binary search will make it faster
        v = pr[q]**3
        if pr[p]*v > N:
            break
        cnt += 1
        if pr[p]*v not in anss:
            #test.append(pr[p]*v)
            anss.add(pr[p]*v)


#print(anss)
print(cnt)        


# AC

