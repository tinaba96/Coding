N = int(input())
A = list(map(int, input().split()))

ans = 0
arr = []
cum = 0

for i in range(N):
    cum += A[i]
    arr.append(cum % 360)

arr.append(0)
arr.append(360)
sarr = sorted(arr)

for i in range(len(sarr)-1):
    ans = max(ans, sarr[i+1]-sarr[i]) 

print(ans)


