def pow_r(x, n):
    """
    O(log n)
    """
    if n == 0:  # exit case
        return 1
    if n % 2 == 0:  # standard case ① n is even
        tmp = pow_r(x ** 2, n // 2)
        #print(tmp)
        return tmp
        #return pow_r(x ** 2, n // 2)
    else:  # standard case ② n is odd
        return x * pow_r(x ** 2, (n - 1) // 2)

A, B, C = list(map(int, input().split()))

f = pow_r(A,C)
s = pow_r(B,C)

print('f :', f)
print('s :', s)

if f > s:
    print(">")
elif f < s:
    print("<")
else:
    print('=')

#print(pow_r(2, 20))
