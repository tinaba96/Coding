#1
A = int(input())
B = int(input())

print(6-A-B)

#2
N = int(input())
S, T = list(map(str, input().split()))

a = []
for i in range(N):
  a.append(S[i])
  a.append(T[i])
print(''.join(a))

#3
A, B = list(map(int, input().split()))
i = 1
if A <= B:
  N = B
  while (N % A) != 0:
    i += 1
    N = B * i
else:
  N = A
  while (N % B) != 0:
    i += 1
    N = A * i
print(N)


#4
N = int(input())
a = list(map(int, input().split()))
if 1 not in a:
  print(-1)
else:
  i = 1
  j = 0
  s = 0
  while j != N:
    if a[j] == i:
      sum = j-i+1
      i += 1
      s = j
    j += 1
  if s != N-1:
    sum += N-s-1
  print(sum)

#5
N = int(input())
class DFactorial(self, n):
  if N < 2:
    return 1
  else:
    return n * DFactorial(n-2)

print(DFactorial(N))

'''
#5ans
N = int(input())
if N%2 == 1:
  print(0)
else:
  i = N//10
  c = 0
  while i != 0:
    c += i
    i = i//5
  print(c)

'''
#6

N, u, v = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(N-1):
  A, B = list(map(int, input().split()))
  graph[A].append(B)
  graph[B].append(A)
#print(graph)

def dfs(v):
  dist = [-1] * (N+1)
  dist[v] = 0
  stack = [v]
 # print(dist)
  while stack:
    now = stack.pop()
    dw = dist[now] + 1
#graph[]は隣接している要素
    for ne in graph[now]:
      if dist[ne] >= 0:
        continue
      dist[ne] = dw
      stack.append(ne)
      #print(ne)
  return dist

Taka = dfs(u)
Ao = dfs(v)

print(Taka)
print(Ao)

ans = 0
for t, a in zip(Taka[1:], Ao[1:]):
  if t < a:
    ans = max(ans, a-1)

print(ans)
