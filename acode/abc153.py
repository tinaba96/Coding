'''

#A
H, A = list(map(int, input().split()))

a = H // A

if H % A == 0:
  print(a)
else:
  print(a+1)


#B


H, N = list(map(int, input().split()))
A = list(map(int, input().split()))


ma = sum(A)

if H <= ma:
  print('Yes')
else:
  print('No')

#C

N, K = list(map(int, input().split()))
H = list(map(int, input().split()))

cnt = 0

if N <= K:
  print(0)
else:
  H.sort(reverse=True)
  H = H[K:]

  cnt += sum(H)

  print(cnt)

#D
H = int(input())

if H == 1:
  print(1)
else:
  cnt = 1

  if H > 2:
    while H >= 2:
      cnt += 1
      H = H/2

    H = 2 ** (cnt-1)

  cnt = H
  two = H

  while two/2 > 1: 
    cnt += two//2
    two = two//2

  print(int(cnt+1))
#上も正解

#Dand
print(2**len(format(int(input()), "b"))-1)


import math
def solve(x):
  if x == 1:
    return 1
  elif x == 0:
    return 0
  else:
    return 2 * solve(math.floor(x/2)) + 1
x = int(input())
print(solve(x))

'''


