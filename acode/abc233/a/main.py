X, Y = list(map(int, input().split()))
if X >= Y:
    print(0)
    exit()
elif (Y-X)%10 == 0:
    print((Y-X)//10)
    exit()
print(int((Y-X)/10+1))


