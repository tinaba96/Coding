L, R, L2, R2 = list(map(int, input().split()))


red = [0 for i in range(101)]
blue = [0 for i in range(101)]

for i in range(L, R):
    blue[i] = 1


for i in range(L2, R2):
    red[i] = 1

ans = 0
for i in range(100):
    if blue[i] == 1 and red[i] == 1:
        ans += 1

print(ans)
