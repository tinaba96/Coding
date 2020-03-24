N = int(input())
arr = list(map(int, input().split()))

def bsort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr

print(bsort(arr))




