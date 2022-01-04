S = str(input())
T = str(input())
s = ord(S[0])-97
t = ord(T[0])-97

diff = t-s
if s > t:
    diff = 26 - (s-t)
#print(diff)

for i in range(len(S)):
    s = ord(S[i])-97
    t = ord(T[i])-97
    if s > t:
        d = 26 - (s-t)
    else:
        d = t-s
    if d != diff:
        print('No')
        exit()
print('Yes')

#print(ord(S)-97)
#print(ord(T)-97)

