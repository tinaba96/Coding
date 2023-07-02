a, b, c = list(map(int, input().split()))

ans = (a+c-1)//c*c

if ans <= b:
    print(ans)
else:
    print(-1)
