ans = 0


for i in range(1,2000001):
  if 1234567890%i == 0:
    print(i)
    ans += i

print(ans)
