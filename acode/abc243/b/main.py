N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                cnt1 += 1
            else:
                cnt2 += 1

print(cnt1)
print(cnt2)



