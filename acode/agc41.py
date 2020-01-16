'''
N, A, B = list(map(int, input().split()))
ans=0
if (B-A)%2 == 0:
  ans = (B-A)//2
else:
  if N-B <= A-1:
    ans += N-B
    A += N-B+1
    ans += (N-A)//2 + 1
  else:
    ans += A-1
    B -= A-1+1
    ans += (B-1)//2 + 1
print(ans)

#B
N, M, V, P = list(map(int, input().split()))
A = list(map(int, input().split()))

for m in range(M):
  for v in range(V):
    A[A.index(min(A))] += 1

for p in range(P-1):
  A.pop(max(A))

print(A)

ma = A.count(max(A))
sa = sorted(set(A))[-2]
mat=A.count(sa-1) + A.count(sa)

ans = ma + mat

print(ans)
'''


N, M, V, P = list(map(int, input().split()))
A = sorted(list(map(int, input().split())), reverse=True)
ans = P

sum_ = [0]*N
sum_[0] = A[0]
for i in range(1,N):
  sum_[i] = (sum_[i-1] + A[i])

for i in range(P, N):
  thre = A[i] + M
  if thre < A[P-1]:
    continue

  remain = V - (P-1) - (N-i)
  if remain <= 0:
    ans += 1
  else:
    if P!=1:
      if sum_[i-1] -sum_[P-2] + M*remain <= thre*(i-P+1):
        ans += 1
    else:
      if sum_[i-1] + M*remain <= thre*(i-P+1):
        ans += 1

print(ans)
