import collections
import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


K = int(input())

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

fac = prime_factorize(K)
ma = max(fac)
c = collections.Counter(fac)

set_f = set(fac)
sf = sorted(fac)

#print(c)
#print(sf)

'''
for a in range(len(sf)):
    if sf[a] in set_f:
'''

#print(c)
ans = ma

for ele in c:
    val = c[ele]
    sp = 0
    if val == 1:
        continue
    cnt = 0
    while val >= 0:
        cnt += 1 #case 2^9, 2 22 222, 222
        if cnt > 2:
            sp += max((ele**(cnt-1) - ele**(cnt-2))//ele - 1, 0) # case 2^3 - 2^2, there is a number that can be divided by 2 between 2^3 and 2^2. this process is to count this
        k = val
        val -= cnt
    print(k)
    print(sp)
    #print(max(0, k-sp))
    add = 0
    if k - sp > 0 :
        add = ele*(k-sp)


    #print(add)
    ans = max(ans, ele**(cnt-1))
    #print(ele**(cnt-1)+add)
    ans = max(ans, ele**(cnt-1)+add)
    


print(ans)

# you can use 197120 as an example
# in this way, number like 12 which can be divided by 2 twice can not be considered well
