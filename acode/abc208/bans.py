import math
#標準入力
s = int(input())
ans = 0

for n in reversed(range(1,11)):
    b = s//(math.factorial(n))
    s = s - b*(math.factorial(n))
    ans = ans + b

print(ans)
