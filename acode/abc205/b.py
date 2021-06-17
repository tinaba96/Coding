N = int(input())
A = list(map(int, input().split()))

arr = []

for i in range(1, N+1):
    arr.append(i)

asort = sorted(A)

if arr == asort:
    print('Yes')
else:
    print('No')


