s = input()
n = int(input())
l = len(s)
q = []
sum = 0
for i,c in enumerate(s):
   if c == "?":
      q.append(2 ** (l-i-1))
   elif c == "1":
      sum += 2 ** (l - i - 1) # sum is kind of base (minimum val)

if sum > n:
   print(-1)
   exit()

for i in q: # similar approach as video editorial
   if sum + i <= n:
      sum += i

print(sum)

