S = list(map(str, input().split()))
T = list(map(str, input().split()))
cnt = 0
for i in range(3):
    if S[i] != T[i]:
        cnt += 1


if cnt == 2:
    print('No')
elif S == T:
    print('Yes')
else:
    print('Yes')


