N,K = map(int,input().split())
A = set(map(int,input().split()))
ans = 0

for i in range(K):
    if i in A:
        ans += 1
    else:
        print(ans)
        exit()

print(ans)
