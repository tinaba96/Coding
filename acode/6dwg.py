'''
def f(s):
  lst = s.split()
  return lst[0], int(lst[1])

N = int(input())
S = []
T = []
for i in range(N):
  s, t = f(input())
  S.append(s)
  T.append(t)

X = str(input())

if X in S:
  index = S.index(X)
else:
  print(o)

sum = 0
for i in range(index+1, N):
  sum += int(T[i])

print(sum)


#print('S',S)
#print('T',T)

'''

#B
N = int(input())
x = list(map(int, input().split()))

def build(location):
  return x[N-1] - x[N - 2 - location]

length = 0

longest = x[N-1] = x[0]

for i in range(N-2):
  longest += build(i)

print(longest)


