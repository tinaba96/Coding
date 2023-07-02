N = int(input())
A = list(map(int, input().split()))
X = int(input())

Asum = sum(A)

times = X//Asum

ans = N*times

XX = X-times*Asum


for i in range(N):
    XX -= A[i]
    if XX < 0:
        print(ans+i+1)
        break


