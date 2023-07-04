N,M = map(int, input().split())
A = []
C = []
for _ in range(M):
  C.append(int(input()))
  n = 0
  for v in list(map(int,input().split())):
    n += 2 ** (v - 1)
  A.append(n)

ans = 0
for i in range(2 ** M):
  sum = 0
  for j in range(M):
    if ( (i>>j) & 1):
      sum = sum | A[j]
  if sum == 2 ** N - 1:
    ans += 1
print(ans)

# video editorial


'''
N,M = map(int,input().split())
S = []
for i in range(M):
  input()
  S.append(list(map(int,input().split())))
ans = 0
correct = [i for i in range(1,N+1)]
for i in range(1, 2 **M):
    p = []
    num = bin(i).split("b")[1]
    num = "0" * ( M - len(num)) + num
    for i in range(M):
      if num[i] == '1':
        p += S[i]
      else:
        continue
    if list(set(p)) == correct:
      ans += 1
print(ans)
'''


