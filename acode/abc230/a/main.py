N = int(input())

if N < 42:
    s = str(N)
    if N < 10:
        print('AGC00' + s)
    else:
        print('AGC0' + s)
else:
    s = str(N+1)
    print('AGC0' + s)


