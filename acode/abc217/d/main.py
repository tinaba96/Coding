import bisect

L, Q = list(map(int, input().split()))
arr = [0, L]
for q in range(Q):
    c, x = list(map(int, input().split()))
    if c == 1:
        #bisect.insort_left(arr, x)
        ind = bisect.bisect_left(arr, x)
        arr.insert(ind, x)  #this is O(N)
    else:
        index = bisect.bisect_left(arr, x)
        diff = arr[index]-arr[index-1]
        print(diff)



