N, M = map(int, input().split())
*a, = map(int, input().split())
a = a + [0]
ans = list(range(1, N + 1))

cnt = 1
for i in range(M):
  if a[i + 1] == a[i] + 1: 
    cnt += 1
  else:
    s = slice(a[i] - cnt, a[i] + 1)
    ans[s] = ans[s][::-1]
    cnt = 1
    
print(*ans)


# similar to video editorial
