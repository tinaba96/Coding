#this is the second solution
# (x - y)^2

n = int(input())

sum = 0
ans = 0

ele = (int(x) for x in input().split())

for i in ele:
  ans += (n - 1) * i * i  # this part represent x^2 + y^2
  ans -= sum * 2 * i  # this part represent -2xy
  sum += i

print(ans)


# it is easier to understand if you expand the formula





