import math
def eratosthenes(n):
    sieve = [True]*(n+1)
    sieve[0],sieve[1] = False,False
    prime = []
    for p in range(2,int(math.sqrt(n))+1,1):
        # if not sieve[p]:
        #     continue
        # q = 2*p
        # while q<=n:
        #     sieve[q] = False
        #     q+=p
        if sieve[p]:
            for i in range(2*p,n+1,p):
                sieve[i] = False
    
    # for i in range(n+1):
    #     if sieve[i]:print(i)
    for i in range(n+1):
        if sieve[i]:
            prime.append(i)
        
    return prime

n = int(input())
m = int(((n//2)**(1/3)+1))
prime = eratosthenes(m)
ans = 0
s = [0]*(m+1)
for p in prime:
    s[p]=1
for i in range(m):
    s[i+1]+=s[i]

for q in prime:
    p = min(q-1,n//(q**3))
    #p = min(q-1,n//q//q//q)
    ans+=s[p]

print(ans)


