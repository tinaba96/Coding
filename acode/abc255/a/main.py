R, C = list(map(int, input().split()))
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

if R == 1:
    if C == 1:
        print(A1[0])
    else:
        print(A1[1])
else:
    if C == 1:
        print(A2[0])
    else:
        print(A2[1])



