'''
N = int(input())

A = [[0]*4]*N

for i in range(N):
  A[i] = list(map(str, input().split()))
  print(A)

B =[ [0]*N]*N
for i in range(N):
  B[i].append(A[i][3])

for i in range(N-1):
  if A[i][0] == A[i+1][0]:
    B.append(A[i+1][3])

print(max(B))

for i in range(N):
  if int(A[i][3]) == max(B[i]):
    print(A[i])

5
2030-01-14 cherrypie 1150 5
2030-01-14 cherrypie 1150 6
2030-01-15 cherrypie 1150 3
2030-01-15 tiramisu 980 2
2030-01-15 burntcream 1980 3
'''

#print(A)


N = int(input())

A = [[0]*4]*N

for i in range(N):
  A[i] = list(map(str, input().split()))

B = []

for i in range(N):
  B.append(A[i][3])

print('B:', B)  
print('Bmax:', max(B))
print('Bslice:', B[:])


print(A[:][3])
print(max(A[3][:]))



