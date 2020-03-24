arr = list(map(int, input().split()))

def qsort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    ref = arr[0]
    ref_cnt = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_cnt += 1

    left = qsort(left)
    right = qsort(right)

    return left + [ref]*ref_cnt + right


print(qsort(arr))







