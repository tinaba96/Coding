'''
#A
s = str(input())
t = str(input())

if s == t:
    print('same')
elif s.lower() == t.lower():
    print('case-insensitive')
else:
    print('different')

#B
N, M, Q = list(map(int, input().split()))
score = [N]*M 
ques = [[0]*M for _ in range(N)]
#print(score)
t = [0]*N
for i in range(N):
    t[i] = []

for i in range(Q):
    ans = 0
    s = list(map(str, input().split()))
    #print('score:', score)
    #print('s0:', s[0])
    #print('q:', ques)
    if int(s[0]) == 2:
        t[int(s[1])-1].append(s[2])
        score[int(s[2])-1] -= 1
        #ques[int(s[1])-1][int(s[2])-1] += 1
        #ques[int(s[2])-1] -= 1
        #score[int(s[2])-1] = [ques[int(s[2])-1]]
        #00print('score:', score[int(s[1])-1])
        #print(score[int(s[1])-1])
    if int(s[0]) == 1:
        #profgor int('score:', score)
        for ele in t[int(s[1])-1]:
            ans += score[int(ele)-1]
        print(ans)

#C
A, R, N  = list(map(int, input().split()))


ans = A

#以下の３つの条件が必要だった。

if R == 1:
    print(A)
    exit()
if A == 0:
    pritn(0)
    exit()
    
if N == 10**9:
    print('large')
    exit()


for i in range(1, N):
    ans = ans*R
    if ans > 10**9:
        print('large')
        exit()
print(ans)


#D
N = int(input())
plate = [[0]*(4*N+1) for _ in range(5)]

for j in range(5):
    s = list(map(str, input().split())) #なぜ文字列ではない？
    for i in range(4*N+1):
        plate[j][i] = s[0][i]


for i in range(1, 4*N+1, 4):
    #print('check:', i)

    if plate[1][i+0] == '#' and plate[0][i+1] == '#' and plate[1][i+1] == '.' and plate[2][i+1] == '.' and plate[3][i+1] == '.':
        print('0', end='')
    if plate[0][i+1] == '#' and plate[1][i+0] == '#' and plate[1][i+1] == '#':
        print('1', end='')
    if plate[3][i+0] == '#' and plate[3][i+2] == '.':
        print('2', end='')
    if plate[1][i+0] == '.' and plate[2][i+0] == '#' and plate[0][i+1] == '#' and plate[3][i+0] == '.' and plate[3][i+2] == '#' and plate[1][i+2] == '#' and plate[2][i+2] == '#':
        print('3', end='')
    if plate[1][i+0] == '#' and plate[2][i+0] == '#' and plate[4][i+0] == '.' and plate[2][i+2] == '#':
        print('4', end='')
    if plate[1][i+0] == '#' and plate[3][i+0] == '.' and plate[1][i+2] == '.' and plate[3][i+2] == '#':
        print('5', end='')
    if plate[1][i+0] == '#' and plate[3][i+0] == '#' and plate[1][i+2] == '.' and plate[2][i+2] == '#':
        print('6', end='')
    if plate[2][i+0] == '.' and plate[4][i+0] == '.':
        print('7', end='')
    if plate[1][i+2] == '#' and plate[3][i+0] == '#' and plate[3][i+2] == '#' and plate[1][i+0] == '#' and plate[2][i+2] == '#' and plate[2][i+1] == '#':
        print('8', end='')
    if plate[1][i+2] == '#' and plate[3][i+0] == '.' and plate[4][i+0] == '#' and plate[3][i+2] == '#' and plate[1][i+0] == '#' and plate[3][i+1] == '.':
        print('9', end='')
print()





#E
N, M, Q = list(map(int, input().split()))
tbl = [[]*(N+1) for _ in range(N+1)]
for i in range(M):
    u, v = list(map(int, input().split()))
    tbl[u].append(v)
    tbl[v].append(u)

c = list(map(int, input().split()))

def coloring(a, col):
    is_colored = True
    for ele in tbl[a]:
        if c[int(ele)-1] != col:
            is_colored = False
        #print(c[int(ele)-1])
        c[int(ele)-1] = col
    if is_colored == True:
        return 0
    #for ele in tbl[a]:
    #    for i in tbl[ele]:
    #        if c[int(i)-1] != col:
    #            coloring(int(i), col)
    for ele in tbl[a]:
        coloring(int(ele), col)

for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        print(c[s[1]-1])
        col = c[s[1]-1]
        coloring(s[1], col)

    if s[0] == 2:
        print(c[s[1]-1])
        c[s[1]-1] = s[2]



N, X, Y = list(map(int, input().split()))
block = []
for i in range(N):
    x, y = list(map(int, input().split()))
    block.append((x, y))
a = X + N
b = Y + N

for i in range(a):
    block.append((i, b))
for j in range(b):
    block.append((a, j))
for i in range(a):
    block.append((i, -N))
for j in range(b):
    block.append((-N, j))

ans = 0
def move(x, y, cnt, ans):
    if x == X and y == Y:
        ans = min(ans, cnt)
        return ans
    if (x, y) in block:
        return 0
    if x > a or y > b:
        return 0
    move(x+1, y+1, cnt+1, ans)
    move(x, y+1, cnt+1, ans)
    move(x-1, y+1, cnt+1, ans)
    move(x+1, y, cnt+1, ans)
    move(x-1, y, cnt+1, ans)
    move(x, y-1, cnt+1, ans)


tmp = move(0, 0, 0, 10**9)
print(tmp)
'''

#F
N = int(input())
a = [[] for _ in range(N)]

for i in range(N):
    x = list(map(str, input().split()))
    for j in range(len(a)):
        if not x[0][j].isdecimal():
            a[i].append(x[0][j])

ans = []
for i in range(len(a)//2+1):
    for ele in a[i]:
        #print('first:', a[i])
        #print('last:', a[-i-1])
        if ele in a[-i-1]:
            ans.append(ele)
            break


ans = ''.join(ans)

if ans != ans[::-1] or ans:
    print('-1')
else:
    print(ans)


#ABCD完答→32点　初級は40点以上
#時間が全然足りない印象

