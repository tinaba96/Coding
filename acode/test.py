import math
A, B, N = list(map(int, input().split()))
ans = 0
if B+1 < N:
    C = B+1
else:
    C = N
if B//A == 0:
    D = 1
else:
    D = B//A
for i in range(1, C+1, D):
    val = math.floor(A*i/B) - A*math.floor(i/B)
    #print("i", i, "val", val)
    ans = max(ans, val)
    print(i)

print(ans)

