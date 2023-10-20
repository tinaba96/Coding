N = str(input())
l = len(N)
Y = N[-1]

if 0 <= int(Y) <= 2:
    print(N[:l-2] + '-')
elif 3 <= int(Y) <= 6:
    print(N[:l-2])
else:
    print(N[:l-2] + '+')


