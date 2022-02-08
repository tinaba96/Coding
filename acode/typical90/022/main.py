A = list(map(int, input().split()))

A.sort(reverse=True)

cnt = 0

#print(A)
while True:
    if A[0] == A[1]== A[2]:
        break
    if A[0] != A[1]:
        A[0] -= A[1]
    else:
        A[1] -= A[2]
    cnt += 1
    A.sort(reverse=True)

print(cnt)

#key is gcd
# O(log(A + B + C))




