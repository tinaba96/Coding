N = int(input())

li = []
for i in range(N):
    a, b, c = list(map(int, input().split()))
    li.append((a, b, c))
mp = [[0 for _ in range(3)] for j in range(N)]
mp[0][0] = li[0][0]
mp[0][1] = li[0][1]
mp[0][2] = li[0][2]


for i in range(1, N):
    mp[i][0] = max(mp[i-1][1]+li[i][0], mp[i-1][2]+li[i][0])
    mp[i][1] = max(mp[i-1][0]+li[i][1], mp[i-1][2]+li[i][1])
    mp[i][2] = max(mp[i-1][0]+li[i][2], mp[i-1][1]+li[i][2])
    #mp[i][0] = max(max(mp[i-1][0]+li[i][0], mp[i-1][1]+li[i][0]), mp[i-1][2]+li[i][0])
    #mp[i][1] = max(max(mp[i-1][0]+li[i][1], mp[i-1][1]+li[i][1]), mp[i-1][2]+li[i][1])
    #mp[i][2] = max(max(mp[i-1][0]+li[i][2], mp[i-1][1]+li[i][2]), mp[i-1][2]+li[i][2])
ans = [mp[N-1][0], mp[N-1][1], mp[N-1][2]]

#print(mp)
print(max(ans))


