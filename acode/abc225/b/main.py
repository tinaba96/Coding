N = int(input())
mp = [0 for i in range(N+1)]

for i in range(N-1):
    a, b = list(map(int, input().split()))
    mp[a] += 1
    mp[b] += 1


for ele in mp:
    if ele == N-1:
        print('Yes')
        exit()
print('No')



