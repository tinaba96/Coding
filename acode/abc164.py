'''
#A
S, W = list(map(int, input().split()))
if W >= S:
    print('unsafe')
else:
    print('safe')

#B

A, B, C, D = list(map(int, input().split()))


if C%B == 0:
    cntA = C//B
else:
    cntA = C//B + 1

if A%D == 0:
    cntC = A//D
else:
    cntC = A//D + 1

if cntA <= cntC:
    print('Yes')
else:
    print('No')

#C
N = int(input())
list = {}
for i in range(N):
    A = str(input())
    list[A] = 1

print(len(list))
'''

#D
S = str(input())
dict = {}
cnt = 0
tot = 0

sum = {}
sum[0] = 0
for i in range(len(S)):
    tot += int(S[i])
    sum[i+1] = tot
#print(sum)


for i in range(len(S)-3):
    for j in range(i+3, len(S)):
        if (sum[j+1]-sum[i])%3 == 0:
            if S[i:j+1] in dict:
                dict[S[i:j+1]] += 1
            else:
                dict[S[i:j+1]] = 1

for ele in dict:
    if int(ele)%2019 == 0:
        cnt += dict[ele]
#print(arr)
print(cnt)
'''
for i in range(len(S)-3):
    for j in range(i+3, len(S)):
        if int(S[i:j+1])%2019 == 0:
            print(S[i:j+1])

'''

