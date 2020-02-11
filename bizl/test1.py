'''
input
1034453893

output
1033344589
'''

N = str(input())
a = []
b = 0
ans = []
for i in range(len(N)):
  a.append(int(N[i]))
a.sort()
for i in range(len(N)):
  if a[i] != 0:
    ans.append(str(a[i]))
  else:
    b += 1
for i in range(b):
  ans.insert(1, '0')

ans = ''.join(ans)
print(ans)



