A, B = list(map(int, input().split()))

ans = 0

mx = max(A, B)
mn = min(A, B)

if mx == 7:
    print(7)
    exit()


if mx == 6:
    if mn == 1 or mn == 3 or mn == 5:
        print(7)
        exit()
    else:
        print(6)
        exit()

if mx == 5:
    if mn == 2 or mn == 3:
        print(7)
        exit()
    else:
        print(5)
        exit()


if mx == 4:
    if mn == 1:
        print(4)
        exit()
    elif mn == 2:
        print(6)
        exit()
    elif mn == 3:
        print(7)
        exit()
    else:
        print(4)
        exit()


if mx == 3:
    if mn == 1:
        print(4)
        exit()
    elif mn == 2:
        print(5)
        exit()
    else:
        print(3)
        exit()

if mx == 2:
    if mn == 1:
        print(3)
        exit()
    else:
        print(2)
        exit()
if mx == 1:
    print(1)
    exit()

print(0)



