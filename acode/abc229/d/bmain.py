S = str(input())
K = int(input())

before = 0
after = 0
between = 0

comp = 0

mp = []

isx = True

for i in range(len(S)):
    if S[i] == '.':
        if isx == False:
            between += 1
        else:
            between = 0

        isx = False
    else:
        if isx == True:
            after += 1
        else:
            before = after
            after = 0
        isx = True


    if between <= K:
        comp = max(comp, between)
        print(comp+before+after)
        exit()





