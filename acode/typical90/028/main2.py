N = int(input())

mp = [[0 for i in range(1000)] for j in range(1000)]

ans[0 for i in range(N)]

for i in range(N):
     lx, ly, rx, ry = list(map(int, input().split()))
     mp[lx][ry] += 1
     mp[rx][ry] -= 1
     mp[lx][ly] -= 1
     mp[rx][ly] += 1

for y in range(1000):
    for x in range(1, 1000):
        mp[x][y] += m[x-1][y] 

for x in range(1000):
    for y in range(1, 1000):
        mp[x][y] += m[x][y-1] 
        ans[mp[x][y]] += 1



