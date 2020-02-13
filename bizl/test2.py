'''
input
Fizz:5 Buzz:2 10

output
Fizz Buzz

Fizz:5 Buzz:2 Fuss:3 qwert:7 300


'''

n = list(map(str, input().split()))
val = int(n[-1])
a = [[]*2]*(len(n)-1)
b = []
c = []
flag = False
for i in range(len(n)-1):
  a[i] = n[i].split(':')
for i in range(len(n)-1):
  if val%(int(a[i][0])) == 0:
    b.append(int(a[i][0]))
    flag = True

b.sort()

for i in range(len(b)):
  for j in range(len(a)):
    if b[i] == int(a[j][0]):
      c.append(a[j][1])

c = ''.join(c)
if flag == True:
  print(c)
else: 
  print(n[-1])
    




