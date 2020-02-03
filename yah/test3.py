N = int(input())

t = list(map(int, input().split()))

su = [0]*(N)
su[0] = t[0]
ans = 0

for i in range(1,N):
  su[i] += su[i-1] + t[i]

for i in range(1,N-1):
  ans += max(su)
  if max(su) == su[1] or max(su) == su[N-2]:
    break
  su[su.index(max(su))] = 0



#su.append(sum(t))

print(su)
print(ans)

'''
24
60 81 44 20 86 94 9 30 15 44 12 87 79 31 80 72 13 80 19 7 18 23 83 96
3853
'''
