N, M = list(map(int, input().split()))

#m = [[0] for i in range(M)] for j in range(M)]

listArr = []
top = []
dic = {}

for i in range(N):
    K = int(input())
    a = list(map(int, input().split()))
    listArr.append(a)
    top.append(a[0])
    if a[0] in dic:
        dic[a[0]] += 1
    else:
        dic[a[0]] = 1


#print(dic)
indexArr = [0] * M 

for k in dic: 
    if dic[k] == 2:
        ind = top.index(k) # it is better to have an array to keep the index instead of this
        top.pop(ind)
        indexArr[ind] += 1
        if listArr[ind][indexArr[ind]] in dic:
        # listArr[ind][indexArr[ind]] is the next item after removing the item
            #dic[listArr[ind][indexArr[ind]]] += 1
            func(listArr[ind][indexArr[ind]])
        else:
            dic[listArr[ind][indexArr[ind]]] = 1
            top.append(listArr[ind][indexArr[ind]])
            
        # for the secoand item
        ind = top.index(k)
        top.pop(ind)
        indexArr[ind] += 1
        if listArr[ind][indexArr[ind]] in dic:
            #dic[listArr[ind][indexArr[ind]]] += 1
            func(listArr[ind][indexArr[ind]])
        else:
            dic[listArr[ind][indexArr[ind]]] = 1
            top.append(listArr[ind][indexArr[ind]])

def func(key):
    dic[key] += 1
    ind = top.index(key)
    top.pop(ind)
    indexArr[ind] += 1
    if listArr[ind][indexArr[ind]] in dic:
        func(listArr[ind][indexArr[ind]])
    else:
        dic[listArr[ind][indexArr[ind]]] = 1
        top.append(listArr[ind][indexArr[ind]])

if top == []:
  print('Yes')
else:
  print('No')

#this is already complex but you need at least another conditional branch whether the cylinder becamoe empty or not.
    

