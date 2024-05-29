N, X, Y = list(map(int, input().split()))

R = [0 for i in range(11)]
B = [0 for i in range(11)]

R[2] = X*Y
B[2] = Y

def B(l):
    if l == 1:
        return 1
    return A(l-1) + B(l-1)*Y
    

def A(l):
    if l == 1:
        return 0
    return A(l-1) + X*B(l)


print(A(N))


