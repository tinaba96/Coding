H, W = map(int, input().split())
r, c = map(int, input().split())

ans = 4
if r == H or c == W:
    ans -= 1
if r == H and c == W:
    ans -= 1
if r == 1 or c == 1:
    ans -= 1
if r == 1 and c == 1:
    ans -= 1


print(ans)


