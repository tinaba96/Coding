S = str(input())

if S[0] == '1':
    print('No')
    exit()

line = [[] for l in range(10)]

line[1].append(S[6])
line[2].append(S[3])
line[3].append(S[1])
line[3].append(S[7])
line[4].append(S[4])
line[4].append(S[0])
line[5].append(S[2])
line[5].append(S[8])
line[6].append(S[5])
line[7].append(S[9])

left = -1
right = -1

for le in range(1, 8):
    f = True
    for e in range(len(line[le])):
        if line[le][e] == '1':
            f = False
    if f == False:
        left = le
        break

for ri in range(7, 0, -1):
    f = True
    for e in range(len(line[ri])):
        if line[ri][e] == '1':
            f = False
    if f == False:
        right = ri
        break


for r in range(2, 7):
    f = True
    ind = 0
    for e in range(len(line[r])):
        if line[r][e] == '1':
            f = False
        
    if f:
        if r > left and r < right:
            print('Yes')
            exit()
        '''
        final = False
        for q in range(len(line[r-1])):
            if line[r-1][q] == '1':
                final = True
        if final == False:
            break
        final = False
        for w in range(len(line[r+1])):
            if line[r+1][w] == '1':
                final = True
        if final:
            print('Yes')
            exit()
        '''
#print(line)

print('No')


