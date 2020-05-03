'''
#A
N = int(input())
A, B = list(map(int, input().split()))

vala = A//N
valb = B//N
if vala != valb or A%N == 0 or B%N == 0:
    print('OK')
elif A == B and N == 1:
    print('OK')
else:
    print('NG')
#B
X = int(input())
val = 100
cnt = 0
while val < X:
    val += val//100
    cnt += 1

print(cnt)

'''
#C
from collections import defaultdict
N, M, Q = list(map(int, input().split()))
ans = 0
table = defaultdict(list)
arr = [[-1]*N for _ in range(N)]

for i in range(Q):
   a, b, c, d = list(map(int, input().split()))
   table[(a,b)] = c

for ele in table:
    if table[0]

print(ans)


'''
#D
import math
A, B, N = list(map(int, input().split()))
ans = 0
if B+1 < N:
    C = B+1
else:
    C = N
if B//A == 0:
    D = 1
else:
    D = B//A
for i in range(1, C+1, D):
    val = math.floor(A*i/B) - A*math.floor(i/B)
    #print("i", i, "val", val)
    ans = max(ans, val)

print(ans)

import math
A, B, N = list(map(int, input().split()))
ans = 0
if B+1 < N:
    C = B+1
else:
    C = N
if B//A == 0:
    D = 1
elif B//A > 1:
  	D = B//A-1
else:
    D = B//A
for i in range(1, C+1, D):
    val = math.floor(A*i/B) - A*math.floor(i/B)
    #print("i", i, "val", val)
    ans = max(ans, val)

print(ans)
'''
