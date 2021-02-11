
N, S, D = list(map(int, input().split()))

for i in range(N):
    X, Y = list(map(int, input().split()))
    if (X < S and Y > D):
        print('Yes')
        exit()

print('No')



