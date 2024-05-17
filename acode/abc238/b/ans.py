# 愚直に問題文通りにピザを回転させた場合

N = int(input())
A = list(map(int, input().split()))

T = [0]
for i in range(N):
    a = A[i]
    for j in range(len(T)):
        t = T[j] + a
        T[j] = t if t < 360 else t - 360
    T.append(0)

T.sort()
ans = 360 - T[-1]
for i in range(len(T)-1):
    ans = max(ans, T[i+1]-T[i])

print(ans)
