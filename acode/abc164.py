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

#using set()
N = int(input())
s = set()
for i in range(N):
    A = str(input())
    s.add(A)

print(len(s))

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



for i in range(len(S)-3):
    for j in range(i+3, len(S)):
        if int(S[i:j+1])%2019 == 0:
            print(S[i:j+1])

'''
#Dans
S = input()[::-1]
dp = [0]*2019
dp[0] = 1

tmp = 0
for i in range(len(S)):
    #modの世界→逆元の概念が難しい
    tmp += int(S[i])*pow(10, i, 2019)
    tmp %= 2019
    dp[tmp] += 1
ans = 0
for i in dp:
    if i >= 2:
        #２つ選ぶ組み合わせ
        ans += i*(i-1)//2
print(ans)


