import math
from collections import defaultdict

A, B = list(map(int, input().split()))

large = 10**18


def fac(x):
    r = defaultdict(int)
    for i in range(2, int(math.sqrt(x)) + 1):
        while x % i == 0:
            x //= i
            r[i] += 1

    if x != 1:
        r[x] += 1
    if len(r) == 0:
        r[x] += 1
    return r

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1):
    # for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

#print(fac(3124) )
#print(factorization(3124) )

## [[2, 3], [3, 1]] 
##  24 = 2^3 * 3^1

factorA = fac(A)
factorB = fac(B) 

#print(factorA)
#print(factorB)

ans = A

for a in factorA:
    cnt = 0
    if a in factorB:
        cnt = max(0, factorB[a]-factorA[a])
        ans *= a**cnt

for b in factorB:
    if b not in factorA:
        ans *= b**factorB[b]


if ans > large:
    print('Large')
else:
    print(ans)
        
    
        
    
# lcm(a, b) = a*b/gcd(a, b)






