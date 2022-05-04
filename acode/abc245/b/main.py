N = int(input())
A = list(map(int, input().split()))

A.sort()
A = list(set(A))

#print(A)

for i in range(len(A)):
    if i != A[i]:
        print(i)
        exit()
print(max(A)+1)

