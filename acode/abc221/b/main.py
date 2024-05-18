S = str(input())
T = str(input())
flag = True
S = list(S)
T = list(T)
for i in range(len(S)):
    if S[i] != T[i]:
        if not flag:
            #(S[i], S[i-1]) = (S[i-1], S[i])
            tmp = S[i]
            S[i] = S[i-1]
            S[i-1] = tmp
            break
        flag = False

if S == T:
    print('Yes')
else:
    print('No')

