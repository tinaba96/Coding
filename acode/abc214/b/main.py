S, T = list(map(int, input().split()))

ans = 0

for a in range(1001):
    if a > S and a > T:
        break
    for b in range(1001):
        if a+b > S and a*b > T:
            break
        for c in range(1001):
            if a+b+c <= S and a*b*c <= T:
                ans += 1
            else:
                break
print(ans)
                



