N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for ele in B:
    if ele not in A:
        print('No')
        exit()
    else:
        A.remove(ele)
print('Yes')

