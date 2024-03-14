N, K = list(map(int, input().split()))
c = list(map(int, input().split()))

arr = set()
ans = 0
for i in range(1+N-K):
    for k in range(K):
        arr.add(c[i+k])
        # print(len, len(arr))
        ans = max(ans, len(arr))

print(ans)
    




