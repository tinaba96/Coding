A, B, C, D = list(map(int, input().split()))
i = 0
if C*D <= B:
    print(-1)
else:
    while True:
        blue = A + B*i
        red = C*i*D
        if blue <= red:
            print(i)
            break
        i += 1



