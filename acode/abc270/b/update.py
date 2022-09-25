X, Y, Z = list(map(int, input().split()))

mx = max(X, 0)
mn = min(X, 0)

if mn < Y and Y < mx:
    if (mn == 0 and Y < Z) or (mx == 0 and Z < Y):
        print(-1)
        exit()
    else:
        print(abs(Z)+abs(X-Z))
        exit()
else:
    print(abs(X))





