N = int(input())

mp = [[0 for i in range(1000)] for j in range(1000)]

for i in range(N):
     lx, ly, rx, ry = list(map(int, input().split()))
     mp[lx][ry] += 1
     mp[rx][ry] -= 1
     mp[lx][ly] -= 1
     mp[rx][ly] += 1

