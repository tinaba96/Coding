A, B, C, X = list(map(int, input().split()))


if X <= A:
    print(1.0000000)
elif B < X:
    print(0.000000)
else:
    print(C/(B-A))

