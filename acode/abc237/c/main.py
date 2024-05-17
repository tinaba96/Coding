S = str(input())

rev = ''.join(list(reversed(S)))

cnt = 0
for i in range(len(S)):
    if S[i] == 'a':
        cnt += 1
        #print('cnt')
    else:
        break
#print(rev)


cnt2 = 0
for i in range(len(S)):
    if rev[i] == 'a':
        cnt2 += 1
        #print('cnt')
    else:
        break
if cnt2 < cnt:
    print('No')
    exit()
#print(S[cnt:len(S)-cnt2])
#print(rev[cnt2:len(S)-cnt])
if S[cnt:len(S)-cnt2] == rev[cnt2:len(S)-cnt]:
    print('Yes')
else:
    print('No')




