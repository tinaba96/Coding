A = list(map(int, input().split()))

B = []

for i in range(len(A)):
  if A[i] in B:
    continue
  elif A[i] != 0:
    B.append(A[i])

L=[str(a) for a in B]
L=" ".join(L)
print(L)




