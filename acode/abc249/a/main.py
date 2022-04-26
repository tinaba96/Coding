A, B, C, D, E, F, X = list(map(int, input().split()))

a = X//(A+C)
b = X//(D+F)

da = a*A*B
db = b*D*E


lefta = X%(A+C)
leftb = X%(D+F)

if lefta >= A:
    da += A*B
else:
    da += lefta*B

if leftb >= D:
    db += D*E
else:
    db += leftb*E

if db < da:
    print("Takahashi")
elif db == da:
    print("Draw")
else:
    print("Aoki")


