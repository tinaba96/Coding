N, M, X, T, D = list(map(int, input().split()))


ini = T-X*D

if M >= X:
    print(X*D+ini)
else:
    print(M*D+ini)



