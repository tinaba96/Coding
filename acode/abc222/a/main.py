N = str(input())
ans = ''
if len(N) == 4:
    print(N)
else:
    ans = str(N)
    cnt = 4 - len(N)
    for i in range(cnt):
        ans = '0'+ans

    print(ans)




