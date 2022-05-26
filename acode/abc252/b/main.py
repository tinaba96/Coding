N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
b = set(B)


maxv = max(A)

for i in range(N):
    if A[i] == maxv and i+1 in b:
        print('Yes')
        exit()


print('No')
