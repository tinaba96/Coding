H, W = map(int, input().split())
r, c = map(int, input().split())

ans = 4
if r == H:
    ans -= 1
if c == W:
    ans -= 1
if r == 1:
    ans -= 1
if c == 1:
    ans -= 1


print(ans)


