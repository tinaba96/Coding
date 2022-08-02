n, c = map(int, input().split())
x = [0] * 31
y = [1] * 31
cnt = [0] * 31
for j in range(31):
    if (c >> j) & 1:
        cnt[-j - 1] = 1
for i in range(n):
    t, a = map(int, input().split())
    if t == 1:
        for j in range(31):
            x[-j - 1] = x[-j - 1] & (a >> j) & 1
            y[-j - 1] = y[-j - 1] & (a >> j) & 1
    elif t == 2:
        for j in range(31):
            x[-j - 1] = x[-j - 1] | (a >> j) & 1
            y[-j - 1] = y[-j - 1] | (a >> j) & 1
    else:
        for j in range(31):
            x[-j - 1] = x[-j - 1] ^ (a >> j) & 1
            y[-j - 1] = y[-j - 1] ^ (a >> j) & 1
    for j in range(31):
        if cnt[j] == 0:
            cnt[j] = x[j]
        else:
            cnt[j] = y[j]
    ans = 0
    for j in range(31):
        if cnt[j] == 1:
            ans += 2 ** (30 - j)
    print(ans)


