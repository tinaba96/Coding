'''
#A
N = str(input())

if '7' in N:
    print('Yes')
else:
    print('No')
#B
N = int(input())
ans = 0
for i in range(1, N+1):
    if i%3 != 0 and i%5 != 0:
        ans += i
print(ans)

#C

K = int(input())
import math
from functools import reduce

def gcd3(a, b, c):
    return math.gcd(math.gcd(a,b), c)
ans = 0

for i in range(1, K+1):
    for j in range(i+1, K+1):
        for k in range(j+1, K+1):
            ans += gcd3(i, j, k)

ans *= 6

for i in range(1, K+1):
    ans += gcd3(i, i, i)

for i in range(1, K+1):
    for j in range(i+1, K+1):
        ans += gcd3(i, i, j)
        ans += gcd3(i, i, j)
for i in range(1, K+1):
    for j in range(i+1, K+1):
        ans += gcd3(i, j, j)
        ans += gcd3(i, j, j)
for i in range(1, K+1):
    for j in range(i+1, K+1):
        ans += gcd3(i, j, i)
        ans += gcd3(i, j, i)
print(ans)
'''

#D
N = int(input())
S = str(input())

ans = 0
'''
for i in range(len(S)):
    if S[i] == 'R':
        for j in range(i+1, len(S)):
            if S[j] != 'R':
                for k in range(j+1, len(S)):
                    if S[k] != 'R' and S[k] != S[j]:
                        if j-i != k-j:
                            ans +=1

for i in range(len(S)):
    if S[i] == 'G':
        for j in range(i+1, len(S)):
            if S[j] != 'G':
                for k in range(j+1, len(S)):
                    if S[k] != 'G' and S[k] != S[j]:
                        if j-i != k-j:
                            ans +=1
for i in range(len(S)):
    if S[i] == 'B':
        for j in range(i+1, len(S)):
            if S[j] != 'B':
                for k in range(j+1, len(S)):
                    if S[k] != 'B' and S[k] != S[j]:
                        if j-i != k-j:
                            ans +=1
'''

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for ele in S:
    if ele == 'B':
        cntb += 1

for ele in S:
    if ele == 'R':
        cntr += 1

for ele in S:
    if ele == 'G':
        cntg += 1

ans = cntb*cntr*cntg



print(ans)
    
