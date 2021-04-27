N, C = list(map(int, input().split()))

arr = [[0 for i in range(3)] for j in range(N)]
for i in range(N):
    a, b, c = list(map(int, input().split()))

    arr[i] = [a, b-a, c]
    
# print(arr)





