import math
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


peop = []
for i in range(N):
    X, Y = list(map(int, input().split()))
    peop.append((X, Y))

ans = 0
for i in range(N):
    mi = 100100100100
    for j in range(K):
        diff = math.sqrt(abs(peop[i][0]-peop[A[j]-1][0])**2 + abs(peop[i][1]-peop[A[j]-1][1])**2)
        mi = min(mi, diff)
    ans = max(ans, mi)




#print(peop[1][0])
print(ans)

