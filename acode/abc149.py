'''
#A
S, T = map(str, input().split())
a = [T, S]
print(''.join(a))

#B
A, B, K = map(int, input().split())

if A >= K:
  A -= K
else:
  B -= (K-A)
  A = 0
if B < 0:
  B = 0
print(A, B)

#C
X = int(input())
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(
        if n % k == 0:
            return False

    return True

while True:
  if is_prime(X) == False:
    X += 1
  else:
    break

print(X)

#D
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = str(input())
A = []
point = 0
for i in range(K):
  if T[i] == 'r':
    A.append('p')
    point += P
  elif T[i] == 's':
    A.append('r')
    point += R
  else:
    A.append('s')
    point += S

for i in range(K, N-K):
  if T[i] == 'r':
    if A[i-K] == 'p':
      if T[i+K] == 's':
        A.append('s')
      else:
        A.append('r')
      continue
    A.append('p')
    point += P
  elif T[i] == 's':
    if A[i-K] == 'r':
      if T[i+K] == 'p':
        A.append('p')
      else:
        A.append('s')
      continue
    A.append('r')
    point += R
  else:
    if A[i-K] == 's':
      if T[i+K] == 'r':
        A.append('r')
      else:
        A.append('p')
      continue
    A.append('s')
    point += S

for i in range(N-K, N):
  if T[i] == 'r':
    if A[i-K] == 'p':
      continue
    A.append('p')
    point += P
  elif T[i] == 's':
    if A[i-K] == 'r':
      continue
    A.append('r')
    point += R
  else:
    if A[i-K] == 's':
      continue
    A.append('s')
    point += S
print(point)

#E
N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
print(A)
sum = 0
extra = M % 3

for i in range(0, M-extra, 3):
  x = A[(i+1)]
  y = A[-i-1]
  sum += x+y
  x = A[-i-1]
  y = A[-i-2]
  sum += x+y
  x = A[-i-2]
  y = A[-i-1]
  sum += x+y
  e = i

if extra == 1:
  x = A[-e-1]
  y = A[-e-1]
  sum += x+y
elif extra == 2:
  x = A[-e-1]
  y = A[-e-1]
  sum += x+y
  x = A[-e-1]
  y = A[-e-2]
  sum += x+y

print(sum)

'''

#Eans

import sys, math, itertools, collect
mans = float('inf')
mod = 10 **9 +7
ans = 0
count = 0
pro = 0

N, M = map(int, input().split())
A = sorted(map(int, input().split())
B = [0] + A[:]
for i in range(N):
  B [i+1] += B[i]
o
#print('A', A)
#print('B', B)
def solve_binary(mid):
  tmp = 0
  for i, ai in enumerate(A):
    tmp += N - bisect.bisect_left(A,
    #bisect.bisect_left(A, mid-ai)は
    #tmpは、aiに固定した時のありうる
  return tmp >= M

def binary_search(N):
  ok = 0
  ng = N
  while abs(ok - ng ) > 1:
    mid = (ok + ng) // 2
    if solve_binary(mid):
      ok = mid
    else:
      ng = mid
  return ok


binresult = binary_search(2*10**5+1)
#Xを二分探索で得る
#binresult=ok
#print(binresult)
for i, ai in enumerate(A):
  ans += ai*(N - bisect.bisect_left(
  #print(ans, '=', ai, '*', N-bisect
  count += N - bisect.bisect_left(A,
ans -= binresult * (count-M)
print(ans)
