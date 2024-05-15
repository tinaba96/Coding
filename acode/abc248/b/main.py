A, B, K = list(map(int, input().split()))

i = 1

val = A*K

if A >= B:
    print(0)
    exit()

while B > val:
    i += 1
    val *= K

print(i)




