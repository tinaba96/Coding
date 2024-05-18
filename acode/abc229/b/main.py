A, B = list(map(str, input().split()))

for i in range(1, min(len(A), len(B))+1):
    numA = int(A[-i])
    numB = int(B[-i])

    if numA + numB >= 10:
        print('Hard')
        exit()

print('Easy')





