'''C = str(input())

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

'''

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





