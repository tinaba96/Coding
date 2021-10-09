P = list(map(int, input().split()))
S = ''
for i in range(len(P)):
  S = S + chr(96 + P[i])
print(S)

'''
p = list(map(int,input().strip().split()))
for i in p:
    print(chr(i+ord('a')-1),end='')
'''
