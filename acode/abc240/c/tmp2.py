N, X = list(map(int, input().split()))

A = []
B = []

for i in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

box = []

a = A[0]
b = B[0]
if (X == a or X == b) and N == 1:
    print('Yes')
    exit()
if a < X:
    box.append(X-a)
if b < X:
    box.append(X-b)


for i in range(1, N):
    a = A[i]
    b = B[i]
    for j in range(len(box)):
        if a < box[j]:
            box[j] -= a
        if b < box[j]:
            box.append(box[j]-b)
    if 0 in box:
        print('Yes')
        exit()
print('No')




