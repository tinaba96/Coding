N = int(input())
A = list(map(int, input().split()))

ans = 0

A.sort(reverse=True)

for i in range(10000):
    if i*A[0] < N:
        continue
    else:
        


#print(A)


