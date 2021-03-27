N = int(input())
x = 1000
ans = 0
while(N >= x):
    ans += N-x+1
    x *= 1000

print(ans)


