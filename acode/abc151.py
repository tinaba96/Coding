'''
C = str(input())

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i, j in enumerate(alph):
  if C == j:
    print(alph[i+1])


#B
N, K, M = list(map(int, input().split()))

A = list(map(int, input().split()))

goal = M*N

sum = 0

for i in range(N-1):
  sum += A[i]
ans = goal - sum
if ans >= 0 and ans <= K :
  print(goal - sum)
elif ans <= 0:
  print(0)
else:
  print(-1)



#C
N, M = list(map(int, input().split()))
P = []
S = []


def f(s):
  lst = s.split()
  return int(lst[0]),lst[1]

for i in range(M):
  p, s = f(input())
  P.append(p)
  S.append(s)

correct = 0
penalty = 0
q = []
p = []

for i, j in enumerate(S):
  if 'AC' in j:
    if P[i] not in q:
      q.append(P[i])
      correct += 1
    else:
      continue
  if 'WA' in j:
    p.append(P[i])
    if P[i] not in q:
        penalty += 1
        if S(P.index(P[i])) != 'AC':
          prenalty -= P.count(P[i])

    else:
      continue

#
for i in range(len(p)):
  if p[i] not in q:
    penalty -= 1
#

print(correct, penalty)


#C ans

N,M = map(int, input().split())

isAC = [0] * (N+1)
isWA = [0] * (N+1)

ACnum = 0
WAnum = 0

for _ in range(M):
    p, s = input().split()
    p = int(p)
    
    if isAC[p] == 1: continue
    if s == 'AC':
        isAC[p] = 1
        ACnum += 1
        WAnum += isWA[p]
    elif s == 'WA':
        isWA[p] += 1

print("%d %d"%(ACnum, WAnum))


#D
from collections import deque

H, W = list(map(int, input().split()))
S = []
for i in range(H):
  l = list(input())
  S.append(l)

q = deque()
dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]
max = 0
for i in range(H):
  for j in range(W):
    dist = [[-1 for m in range(W)] for n in range(H)]
    dist[i][j] = 0
    if S[i][j] =="#":
      continue

    q.append((i, j))
    while q:
      sh, sw = q.popleft()
      for k in range(4):
        ah = sh + dh[k]
        aw = sw + dw[k]

        if 0 <= ah < H and 0 <= aw < W:
          if S[ah][aw] == "#":
            continue
          if dist[ah][aw] == -1:
            q.append((ah,aw))
            dist[ah][aw] = dist[sh][sw] + 1
            if dist[ah][aw] > max:
              max = dist[ah][aw]

print(max)
'''

#F
N = int(input())
l = []
for i in range(N):
    x, y = [int(j) for j in input().split()]
    l.append((x,y))

#determine the function representing the longest distance ^2 from the center point to designated N points.
#中心からの距離(半径)、x軸とy軸でそれぞれ考えている。
def loss(x,y):
    maxi = 0
    #最大の距離
    for i, j in l:
        maxi = max(maxi, (i-x)**2 + (j-y)**2)
    return maxi

def f(x):
    #return min l(x, y)
    left = 0
    right = 1000
    num = 100

    for i in range(num):
        c1 = (2*left + right)/3
        c2 = (left + 2*right)/3
        if (loss(x, c1)<loss(x,c2)):
            right = c2
        else:
            left = c1
    return loss(x, left)

left = 0
right = 1000
num = 100

for i in range(num):
    c1 = (2*left + right)/3
    c2 = (left + 2*right)/3
    if (f(c1)<f(c2)):
        right = c2
    else:
        left = c1

ans = f(left)**0.5
print(ans)

#low space complexoty but high time complexity
#there other way of coding that is low time complexity but high space complexity
#it is shown bellow

'''
import sys
import itertools
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
XY = [lr() for _ in range(N)]
XY = [x + y * 1j for x, y in XY]

cen_cand = [] # list of candidates which is center of a cercle
'''
z = (ab(a-b).conjugete()) / (a.conjugate()*b-a*b.conjugate())
'''
def find_center(a, b, c):
    #cを原点とする
    a -= c; b -= c
    if abs((a * b.conjugate()).imag) < 0.5:
        # 同一直線上
        return None
    num = a * b * (a-b).conjugate()
    den = a.conjugate() * b
    den -= den.conjugate()
    return (num / den) + c

for comb in itertools.combinations(XY, 3):
    o = find_center(*comb)
    if o is None:
        continue
    cen_cand.append(o)

for a, b in itertools.combinations(XY, 2):
    o = (a+b) / 2
    cen_cand.append(o)

cen_cand = np.array(cen_cand); XY = np.array(XY)
answer = np.abs(cen_cand[:, None] - XY[None, :]).max(axis=1).min()
print(answer)
# 28

'''










