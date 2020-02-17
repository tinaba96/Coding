'''
#A
A, B, C = list(map(int, input().split()))


if (A == B or B == C or A == C):
  if A == B and B == C and C == A:
    print('No')
  else:
    print('Yes')
else:
  print('No')

#B
N = int(input())
A = list(map(int, input().split()))
flag = 'ap'
for i in range(N):
  if A[i]%2 == 0:
  if A[i]%3 == 0 or A[i]%5 == 0:
      continue
    else:
      flag = 'den'

if flag == 'ap':
  print('APPROVED')
else:
  print('DENIED')

'''
#C
N = int(input())
A = []
B = []
asort = []
for i in range(N):
  A.append(str(input()))
asort = list(set(A))
asort.sort()

for i in range(len(asort)):
  B.append(A.count(asort[i]))
#print(B)
#print(max(B))
ma = max(B)
#print(B.index(ma))
if not N:
  print(0)
while ma in B:
  print(A[B.index(ma)])
  B[B.index(ma)] = 0
  #print(B)


'''
#D
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
#print(N)
#case = (N(N-1))/2
com = []
cnt = 0
maxval = A[-1]
if K >= case:
  for i in range(N):
    com.append
  com = 


for i in range(N):
  for j in range(i+1, N):
    com.append(A[i]*A[j])

com.sort()
#print(com)
print(com[K-1])
'''
