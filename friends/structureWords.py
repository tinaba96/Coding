N = int(input())
S = str(input())

vowel = 'AUIOU'
input_vowel = set()
input_consonant = set()
cnt_vowel = 0
cnt_consonant = 0

for i in range(N):
    if S[i] in vowel:
        input_vowel.add(S[i])
        cnt_vowel += 1
    else:
        input_consonant.add(S[i])
        cnt_consonant += 1

#print(input_vowel)
#print(input_consonant)

len_vowel = len(input_vowel)
len_consonant = len(input_consonant)

# in case of return 0
if abs(cnt_vowel-cnt_consonant) > 1:
    print(0)
    exit()


ans = cnt_consonant #first letter should be a consonant

for v in range(1, cnt_vowel+1):
    ans *= v

for c in range(1, cnt_consonant):
    ans *= c


# consider duplicate
d_vowel = cnt_vowel-len_vowel
d_consonant = cnt_consonant-len_consonant

if d_vowel > 0:
    for dv in range(1, d_vowel+2):
        ans /= dv

if d_consonant > 0:
    for dc in range(1, d_consonant+2):
        ans /= dc


print(int(ans))


    
    

