N = int(input())
arr = []
# u can also use string instead of array
while N > 0:
    if N % 2 == 1:
        arr.append('A')
        N -= 1
    else:
        arr.append('B')
        N = N//2

arr.reverse()
print(''.join(arr))




