A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = set()
a = set()

a.add(A[0])
a.add(B[0])
a.add(C[0])

for i in range(2):
    if A[i] in s:
        s.remove(A[i])
    else:
        s.add(A[i])
for i in range(2):
    if B[i] in s:
        s.remove(B[i])
    else:
        s.add(B[i])
for i in range(2):
    if C[i] in s:
        s.remove(C[i])
    else:
        s.add(C[i])

S = list(s)
if S[0] in a:
    print(S[0], S[1])
else:
    print(S[1], S[0])



