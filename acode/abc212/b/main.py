A = str(input())

x1 = A[0]
x2 = A[1]
x3 = A[2]
x4 = A[3]


n1 = int(A[0])
n2 = int(A[1])
n3 = int(A[2])
n4 = int(A[3])


if x1 == x2 and x2 == x3 and x3 == x4:
    print('Weak')
    exit()
elif (n2 == n1+1 or (n2 == 0 and n1 == 9) ) and (n3 == n2+1 or (n3 == 0 and n2 == 9) ) and (n4 == n3+1 or ( n4 == 0 and n3 == 9)):
    print('Weak')
else:
    print('Strong')


