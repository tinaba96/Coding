N = int(input())
A = list(map(int, input().split()))

#print(A)
rev = list(reversed(A))
s = set()

for a in range(N):
    if A[a] != rev[a]:
        s.add(A[a])
if len(s) == 0:
    print(0)
else:
    print(len(s)-1)


