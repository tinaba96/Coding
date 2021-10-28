N = str(input())

arr = []


for i in range(len(N)):
    s = N[i:] + N [:i]
    arr.append(s)
arr.sort()
#print(arr)

print(arr[0])
print(arr[-1])

# O(N^2)


