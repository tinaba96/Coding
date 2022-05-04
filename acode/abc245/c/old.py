import sys
sys.setrecursionlimit(10**6)


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def build(i, v):
    if i == N:
        print('Yes')
        exit()

    if abs(A[i]-v) <= K:
        build(i+1, A[i])

    if abs(B[i]-v) <= K:
        build(i+1, B[i])

flagA = True
flagB = True

for i in range(N-1):
    if flagB == False and flagA == True:
        if abs(A[i]-A[i+1]) > K and abs(A[i]-B[i+1]) > K:
            print('No')
        elif abs(A[i]-A[i+1]) <= K:
            flagA = True
        elif abs(A[i]-B[i+1]) <= K:
            flagB = True

    if flagA == False and flagB == True:
        if abs(A[i]-A[i+1]) > K and abs(A[i]-B[i+1]) > K:
            print('No')
        elif abs(A[i]-A[i+1]) <= K:
            flagA = True
        elif abs(A[i]-B[i+1]) <= K:
            flagB = True



    if flagA:
        if abs(A[i]-A[i+1]) > K and abs(B[i]-A[i+1]) > K:
            flagA = False

    if flagB:
        if abs(A[i]-B[i+1]) > K and abs(B[i]-B[i+1]) > K:
            flagB= False

    

    if abs(A[i]-A[i+1]) > K and abs(A[i]-B[i+1]) > K:
        if abs(B[i]-A[i+1]) > K and abs(B[i]-B[i+1]) > K:
            print('No')
            exit()

print('Yes')



#build(1, A[0])
#build(1, B[0])

#print('No')

