X, Y, Z = list(map(int, input().split()))

mx = max(X, 0)
mn = min(X, 0)

if mn < Y and Y < mx:
    if (mn == 0 and Y < Z) or (mx == 0 and Z < Y):
        print(-1)
        exit()
    elif mn == 0 and Z < mn:
        print(abs(X)+2*abs(Z))
        exit()
    elif mx == 0 and mx < Z :
        print(abs(X)+2*abs(Z))
        exit()
    else:
        print(abs(X))
        exit()
else:
    print(abs(X))





