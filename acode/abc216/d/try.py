import sys
#import resource

sys.setrecursionlimit(1000000000)
N, M = list(map(int, input().split()))

#m = [[0] for i in range(M)] for j in range(M)]

listArr = []
top = [0 for m in range(M+1)]
dic = [0 for i in range(N+1)]

keepSize = [0 for i in range(N)]

for i in range(M):
    K = int(input())
    a = list(map(int, input().split()))
    listArr.append(a)
    top[i] = a[0]
    keepSize[i] = K
    dic[a[0]] += 1

def func(key):
    #print(top)
    dic[key] = 0

    ind = top.index(key)
    top[ind] = 0
    indexArr[ind] += 1
    if indexArr[ind] < keepSize[ind]:
        top[ind] = listArr[ind][indexArr[ind]]
        if dic[listArr[ind][indexArr[ind]]] == 1:
            func(listArr[ind][indexArr[ind]])
        else:
            dic[listArr[ind][indexArr[ind]]] = 1

    ind = top.index(key)
    top[ind] = 0
    indexArr[ind] += 1
    if indexArr[ind] >= keepSize[ind]:
        return
    top[ind] = listArr[ind][indexArr[ind]]
    if dic[listArr[ind][indexArr[ind]]] == 1:
        top[ind] = listArr[ind][indexArr[ind]]
        func(listArr[ind][indexArr[ind]])
    else:
        dic[listArr[ind][indexArr[ind]]] = 1


#print(dic)
indexArr = [0] * M 

for k in range(N): 
    if dic[k] == 2:
        ind = top.index(k) # it is better to have an array to keep the index instead of this
        top[ind] = 0
        indexArr[ind] += 1
        if indexArr[ind] < keepSize[ind]:
            #print('listArr', listArr[ind][indexArr[ind]])
            #print('indArr[ind]', indexArr[ind])
            #print('ind', ind)
            top[ind] = listArr[ind][indexArr[ind]]
            if dic[listArr[ind][indexArr[ind]]] == 1:
            # listArr[ind][indexArr[ind]] is the next item after removing the item
                #dic[listArr[ind][indexArr[ind]]] += 1
                func(listArr[ind][indexArr[ind]])
            else:
                dic[listArr[ind][indexArr[ind]]] = 1
            
        # for the secoand item
        ind = top.index(k)
        top[ind] = 0
        indexArr[ind] += 1 #check
        if indexArr[ind] < keepSize[ind]:
            top[ind] = listArr[ind][indexArr[ind]]
            if dic[listArr[ind][indexArr[ind]]] == 1:
                #dic[listArr[ind][indexArr[ind]]] += 1
                func(listArr[ind][indexArr[ind]])
            else:
                dic[listArr[ind][indexArr[ind]]] = 1


#print(top)
flag = True
for i in range(len(top)):
    if top[i] != 0:
        flag = False

if flag:
    print('Yes')
else:
    print('No')

#this is already complex but you need at least another conditional branch whether the cylinder becamoe empty or not.

# O(MK) ?

    

