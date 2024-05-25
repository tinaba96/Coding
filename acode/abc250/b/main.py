N, A, B = list(map(int, input().split()))

ans = [["." for i in range(N*B)] for j in range(N*A)]

#print(ans)
for i in range(N*A):
    if (i//A)%2 == 1:
        for j in range(0, N*B, 2*B):
            for k in range(B):
                ans[i][j+k] = "#"
    else:
        for j in range(B, N*B, 2*B):
            for k in range(B):
                ans[i][j+k] = "#"

for i in range(N*A):
    print("".join(ans[i]))

