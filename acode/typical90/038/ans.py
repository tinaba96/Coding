A, B = map(int, input().split())

def gcd(a, b):
    if a < b: a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

l = A // gcd(A, B)
if l > 10**18 // B:
    print('Large')
else:
    print(l * B)

# lcm(a, b) = a*b/gcd(a, b)
