import copy
import math
import collections
def comb(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))
#A
'''
N, M = list(map(int, input().split()))
a, b = 0, 0
if N >= 2:
    a = comb(N, 2)
if M >= 2:
    b = comb(M, 2)
ans = a + b
print(ans)

#B
S = str(input())
N = len(S)
A = S[0:((N-1)//2)]
B = S[(N+3)//2-1:N]
if S == S[::-1] and A == A[::-1] and B == B[::-1]:
    print('Yes')
else:
    print('No')

#C
L = int(input())
ans = 0
l = L/3
print(l**3)

'''

#D
N = int(input())
A = list(map(int, input().split()))
count = collections.Counter(A)
ans = [0]*N
for i in range(2,N):
    ans[i] = comb(i, 2)
#print(ans)
for i in range(N):
    arr = copy.copy(count)
    arr[A[i]] -= 1
    cnt = 0
    #print(count)
    for num in count:
        cnt += ans[arr[num]]
    #print(cnt)

#Dans
from collections import Counter

N = int(input())
A = list(map(int, input().split()))


def comb(x):
    if x == 0:
        return 0
    if x == 1:
        return 0
    return x * (x - 1) // 2


d = Counter(A)
# print(d)
k = d.keys()

# print(k)
total = 0

for kk in k:
    total += comb(d[kk])

# print(total)

for a in A:
    res = total
    res -= comb(d[a])
    res += comb(d[a] - 1)
    print(res)


'''
    print(cnt)
    for j in range(N):
        if arr[j] >= 2:
           cnt += comb(arr[j],2)
'''
    






