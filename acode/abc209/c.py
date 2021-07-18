N = int(input())
C = list(map(int, input().split()))

ans = 1
#print(C)
i = 0

C.sort()

for c in range(N):
    ans *= C[c]-i
    ans = ans%(10**9+7)
    i += 1

print(ans%(10**9+7))


