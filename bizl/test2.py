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
for i in range(len(n)-1):
  a[i] = n[i].split(':')
for i in range(len(n)-1):
  if val%(int(a[i][1])) == 0:
    b.append(a[i][0])

b = ' '.join(b)

print(b)
    




