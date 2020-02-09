'''
n = int(input())
s = 0
for i in range(1,1+n):
    s += (i)*(1/n)
print(s)

'''
#D
N, K = list(map(int, input().split()))
P = list(map(int, input().split()))
p = 0
ma = 0
for i in range(0,N-K+1):
  q = 0
  for j in range(K):
    q += P[j+i]
  if ma < q:
    p = i
    ma = q
s = 0
for i in range(p, p+K):
  for j in range(1, 1+P[i]):
    s += (j)*(1/P[i])
print(s)

'''
#A

S, T = list(map(str, input().split()))
A, B = list(map(int, input().split()))
U = str(input())

s = A
t = B

if U == S:
  s -= 1
else:
  t -= 1

print(s, t)


#C

s = str(input())
a = []
for i in range(len(s)):
  a.append('x')
  
print(''.join(a))

#C

N = int(input())

A = list(map(int, input().split()))
A.sort()
flag = True
for i in range(N-1):
  if A[i] == A[i+1]:
    flag = False
if flag == True:
  print('YES')
else:
  print('NO')
'''
