N = int(input())
A = list(map(int, input().split()))
ans = [] 
for i in range(1, N+1):
    l = 0 
    r = N
    while l > r:
        m = (r+l)/2






ans =' '.join(ans)
print(ans)

