import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')


N, A, B = list(map(int, input().split()))
S = str(input())

ans = N*B

import collections

c = collections.Counter(S)

val = 0

cntSingle = 0
cntP = 0

for e in c:
    #print(c[e])
    if c[e] % 2 != 0:
        cntSingle += 1
    cntP += c[e] // 2

#print(cntSingle)
numB = cntSingle // 2

need = N // 2 - cntSingle

base = B*numB


def ch(g):
    cnt = 0
    for k in range(len(g)):
        if k > len(g) // 2 - 1:
            break
        if g[k] == g[len(g)-1-k]:
            cnt += 1
    return cnt

jo = S + S
#print(jo)
#print(jo[:N])
cntVal = 0

for j in range(N):
    am = ch(jo[j:N+j])
    #print(am)
    
    #if  am >= 1:
    whi = min(B*am, A*j) #this is to check whether A is right dicision than B -> if B is better, this will be convered by another loop 
    numBB = (cntP - am)*B
    #print(numBB)
    ans = min(ans, whi + numBB) 

#print(base)
#print(ans)
print(base+ans)

# similar to the ans (video editorial) but this is more complex

