L, R, L2, R2 = list(map(int, input().split()))

if L <= L2 and R2 <= R:
    print(abs(R2-L2))
    exit()
if L2 <= L and R <= R2:
    print(abs(R-L))
    exit()

if L >= R2 or R <= L2:
    print(0)
    exit()
else:
    if L2 < R:
        print(abs(L2-R))
        exit()
    elif L < R2:
        print(abs(L-R2))
        exit()

print(0)

