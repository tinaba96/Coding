from math import gcd
A, B, C = map(int, input().split())
L = gcd(gcd(A, B), C)
print(A // L + B // L + C // L - 3)

