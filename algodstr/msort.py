arr = list(map(int, input().split()))

def msort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = msort(left)
    right = msort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    li = 0
    ri = 0

    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1

    if li < len(left):
        merged.extend(left[li:])
    if ri < len(right):
        merged.extend(right[ri:])
    return merged

print(msort(arr))
