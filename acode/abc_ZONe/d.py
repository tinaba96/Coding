S = str(input())
flag = True
T = []
#left = S[0]
#right = S[1]
#T.append(left)
#T.append(right)
'''
for e in range(2,len(S)):
    if right != S[e]:
        right = S[e]
    else:
        T.pop(1)
        if len(T) >= 1:
            right = T[0]
        else 
        right = 0
'''
s = 0
while True:
    if s >= len(S):
        break
    if s <= len(S)-2:
        if S[s] != 'R' and S[s] == S[s+1]:
            s += 2
            continue
    
    if S[s] == 'R':
        flag = not flag
    else:
        if flag:
            if len(T) > 0 and T[-1] == S[s]:
                #T.pop(-1)
                del T[-1]
            else:
                T.append(S[s])
        else:
            if len(T) > 0 and T[0] == S[s]:
                #T.pop(0)
                del T[0]
            else:
                T.insert(0, S[s])
    s += 1


'''
f = True
while True:

    ind = []
    #print('T',T)


    for t in range(1, len(T)):
        if T[t] == T[t-1]:
            ind.append(t)
            ind.append(t-1)
    # print('ind', ind)        
    if len(ind) == 0:
        break
    else:
        ind.sort()

    index = 0
    for ele in ind:
        T.pop(ele-index)
        index += 1
'''
T = ''.join(T)

if not flag:
    print(T[::-1])
else:
    print(T)






