N = int(input())
S = str(input())
Q = int(input())


for q in range(Q):
    t, a, b = list(map(int, input().split()))

    if ( t == 1):
        # S = S[:a]+S[b]+S[a:b]+S[b:]
        S = S[:a-1]+S[b-1]+S[a:b-1]+S[a-1]+S[b:]
    else:
       S = S[N:]+S[:N]
    # print(S)


print(S)




