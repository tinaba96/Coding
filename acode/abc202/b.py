S = str(input())


S = S[::-1]

SS = []

for i in range(len(S)):
    if S[i] == "6":
        SS.append("9")
    elif S[i] == "9":
        SS.append("6")
    else:
        SS.append(S[i])


print(''.join(SS))

