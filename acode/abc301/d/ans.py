def get_primes(N):
  if N==1: return []
  if N==2: return [2]
  primes = [2]
  fl=[False]*(N+1)
  for i in range(N+1):
    if i%2==0:fl[i]=True
  for i in range(3, N+1,2):
    if fl[i]: continue
    primes.append(i)
    for j in range(i, N+1, i):
      fl[j]=True
  return primes

N=int(input())
primes = get_primes(int((N/12)**0.5)+1)
ans=0
for i in range(len(primes)):
  if primes[i]**5>N: break
  for j in range(i+1, len(primes)):
    if (primes[i]**2)*(primes[j]**3)>N: break
    for k in range(j+1, len(primes)):
      p1 = primes[i]
      p2 = primes[j]
      p3 = primes[k]
      if p1*p1*p2*p3*p3<=N:
        ans+=1
      else:
        break
print(ans)
