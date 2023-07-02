A, B, C = list(map(int, input().split()))


tmp = A//C

val = (tmp+1)*C

if val <= B:
    print(val)
else:
    if A%C == 0:
        print(A)
    else:
       print(-1)



