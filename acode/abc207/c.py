N = int(input())

mp = [[0,0] for j in range(N)]

for n in range(N):
    a, b, c = list(map(int, input().split()))

    if a == 1:
        mp[n][0] = b
        mp[n][1] = c
    if a == 2:
        mp[n][0] = b
        mp[n][1] = c-0.5
    if a == 3:
        mp[n][0] = b+0.5
        mp[n][1] = c
    if a == 4:
        mp[n][0] = b+0.5
        mp[n][1] = c-0.5

cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        if mp[i][1] < mp[j][0]:
            continue
        elif mp[i][0] > mp[j][1]:
            continue
        else:
            cnt += 1

print(cnt)
