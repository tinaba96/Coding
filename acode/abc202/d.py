import itertools

A, B, K = list(map(int, input().split()))
arr = []
for i in range(A):
    arr.append('a')

for i in range(B):
    arr.append('b')

print(arr)

arr = ['a', 'b']
t = list(itertools.permutations(arr,2))

print(t)

print(bin(118264581564861424))

