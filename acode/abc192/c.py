N, K = list(map(int, input().split()))


def diff(n):
    arr = []
    st = str(n)
    for s in st:
        arr.append(s)
    arr.sort()
    small_ans = ''.join(arr)
    barr= sorted(arr, reverse=True)
    big_ans =''.join(barr)
    ans = int(big_ans) - int(small_ans)

    #print(ans)
    return ans

tmp = N
for i in range(K):
    tmp = diff(tmp)
print(tmp)

