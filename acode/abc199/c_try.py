N = int(input())
S = list(str(input()))
Q = int(input())
# print(S)
flag = True


for i in range(Q):
    t, a, b = list(map(int, input().split()))

    if t==1:
        if flag:
            tmpa = S[a-1]
            tmpb = S[b-1]

            S[a-1] = tmpb
            S[b-1] = tmpa

        else:
            a = (a+N)%(2*N)
            b = (b+N)%(2*N)
            tmpa = S[a-1]
            tmpb = S[b-1]

            S[a-1] = tmpb
            S[b-1] = tmpa
    else:
        flag = not flag

if not flag:
    t = S[N:]
    t.extend(S[:N])
    # print(t)
    print(''.join(t))
else:
    print(''.join(S))

