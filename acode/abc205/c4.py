A, B, C = list(map(int, input().split()))

#f = A**C
#s = B**C

if C%2 == 0:
    if abs(A) > abs(B):
        print(">")
    elif abs(A) < abs(B):
        print("<")
    else:
        print('=')
else:
    if A < 0 and B < 0:
        if abs(A) > abs(B):
            print("<")
        elif abs(A) < abs(B):
            print(">")
        else:
            print('=')
    elif A < 0 and B >= 0:
        print("<")
    elif B < 0 and A >= 0:
        print('>')
    else:
        if abs(A) > abs(B):
            print(">")
        elif abs(A) < abs(B):
            print("<")
        else:
            print('=')

            



