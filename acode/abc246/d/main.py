N = int(input())


a = 10**6
b = 10**6
Xb = a**3 + a**2*b + a*b**2 + b**3

a = 10**6-1
b = 10**6-1
Xa = a**3 + a**2*b + a*b**2 + b**3
#print('a',Xb-Xa)
val = 0
fa = 0
fb = 0
#print(5**3*3)

if N == 0:
    print(0)
    exit()

b = 0
for i in range(10**6):
    a = i
    X = a**3 + a**2*b + a*b**2 + b**3
    #print(X)
    if X < N:
        val = X
        fa = a
    else:
        break

for i in range(10**6):
    b = i
    Xn = X + fa**3 + fa**2*b + fa*b**2 + b**3
    if Xn >= N:
        val = Xn
        fb = b
        break

for i in range(10**6):
    fa -= i
    Xf = fa**3 + fa**2*fb + fa*fb**2 + fb**3
    if Xf >= N:
        val = Xf
        fb = b
        break

print(val)

