N, K, A = list(map(int, input().split()))

p = K % N 
if p == 0:
    if A-1 > 0:
        print(A-1)
    else:
        print(N)
    exit()
p -= 1

if p + A > N:
    print(p+A-N) # samae as print((A+K-1)%N)
else:
    print(p+A)



#print(max(A+K, A+K-N))


