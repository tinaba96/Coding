ans = 0

for i in range(1, 30001):
  if i%3 == 0:
    ans += i
    continue
  if i > 10000 and (i//10000 == 3 or (i//1000)%10 == 3 or (i//100)%10 == 3 or (i//10)%10 == 3 or i%10 ==3):
    ans += i
    continue
  if i > 1000 and (i//1000 == 3 or (i//100)%10 == 3 or (i//10)%10 == 3 or i%10 == 3):
    ans += i
    continue
  if i > 100 and (i//100 == 3 or (i//10)%10 == 3 or i%10 ==3):
    ans += i
    continue
  if i > 10 and (i//10 == 3 or i%10 == 3):
    ans += i
    continue
  if i > 1 and i == 3:
    ans += i
    continue

print(ans)
