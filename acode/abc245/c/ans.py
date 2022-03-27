from sys import stdin

n, k = map(int, input().split())
data = [stdin.readline().rstrip().split() for _ in range(2)]

dp = [False] * n
ep = [False] * n
# print(dp)
a = list(map(int, data[0]))
b = list(map(int, data[1]))

dp[0] = True
ep[0] = True

for i in range(1, n):
    if dp[i-1] == True:
        if abs(a[i-1] - a[i]) <= k:
            dp[i] = True
        if abs(a[i-1] - b[i]) <= k:
            ep[i] = True
    if ep[i-1] == True:
        if abs(b[i-1] - b[i]) <= k:
            ep[i] = True
        if abs(b[i-1] - a[i]) <= k:
            dp[i] = True

if dp[n-1] == True or ep[n-1] == True:
    print("Yes")
else:
    print("No")
