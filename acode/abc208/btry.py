# from atcoder

P = int(input())

ans = 0
x = 2
while P > 0:
    ans += P%x
    P = P//x
    x += 1

print(ans)


