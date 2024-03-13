h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

ans = 0
for i in range(h-1):
    for j in range(w-1):
        count = 0
        for ii in range(2):
            for jj in range(2):
                if s[i+ii][j+jj] == '#':
                    count += 1
        if count == 1 or count == 3:
            ans += 1

print(ans)


