A = list(map(int, input().split()))
A=sorted(A)
if ( abs(A[0]-A[1]) == abs(A[1]-A[2])):
        print('yes')
else:
        print('No')

