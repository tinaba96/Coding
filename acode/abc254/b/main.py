N = int(input())


tmp = [1]

print(*tmp)
for i in range(1, N):
    now = []
    for j in range(i+1):
        if j == 0 or j == i:
            now.append(1)
        else:
            now.append(tmp[j-1]+tmp[j])

    print(*now)
    tmp = now



