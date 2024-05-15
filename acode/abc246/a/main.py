A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

s = set()
a = set()
b = set()

a.add(A[0]) #x
if B[0] in a:
    a.remove(B[0])
else:
    a.add(B[0])
if C[0] in a:
    a.remove(C[0])
else:
    a.add(C[0])

b.add(A[1]) #y
if B[1] in b:
    b.remove(B[1])
else:
    b.add(B[1])
if C[1] in b:
    b.remove(C[1])
else:
    b.add(C[1])

'''
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
'''

aa = list(a)
bb = list(b)
print(aa[0], bb[0])

