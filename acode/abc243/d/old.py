N, X = list(map(int, input().split()))
S = str(input())
SS = [S[0]]

c = 1
while True:
    if S[c] == 'U':
        if S[c-1] != S[c+1]:
            SS.append(S[c])
        else:
            SS.pop()
            c += 1

    else:
        SS.append(S[c])
    c += 1
    if c == N-1:
        break


SS.append(S[-1])
print(SS)

for i in range(len(SS)):
    if SS[i] == 'U':
        X  = X // 2
    if SS[i] == 'L':
        X *= 2
    if SS[i] == 'R':
        X = 2*X + 1


print(X)
    



