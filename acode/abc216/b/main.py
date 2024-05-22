N = int(input())
arr = []
for i in range(N):
    s, t = list(map(str, input().split()))
    if (s,t) in arr:
        print('Yes')
        exit()
    arr.append((s, t))
        


print('No')






