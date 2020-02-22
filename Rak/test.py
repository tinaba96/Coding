def solution(A, B, C):
    arr={}
    ans = []
    arr["a"]=A
    arr["b"]=B
    arr["c"]=C
    temp = [A, B, C]
    Aar = []
    Bar = []
    Car = []
    final = []

    arrdict = sorted(list(arr.items()))
    '''
    for i in range(A+B+C):
        arrdict.sort(key=lambda x:x[1], reverse = True) 
        ans.append(arrdict[0][0])
        arrdict.pop()
    '''


    arrdict.sort(key=lambda x:x[1], reverse = True) 
    for i in range(arrdict[0][1]):
        ans.append(arrdict[0][0])
    
    temp.pop(temp.index(max(temp)))
    ind = 0
    for i in range(arrdict[1][1]):
        ans.insert((2*(i+1)+ind), arrdict[1][0])
        ind += 1

    arrdict.sort(key=lambda x:x[1], reverse = True) 
    for i in range(arrdict[0][1]):
        ans.append(arrdict[0][0])

    
    for i in range(arrdict[2][1]):
        ans.insert((ind), arrdict[2][0])
        ind += 2*(i+2)


    return ''.join(ans)



print(solution(2, 6, 2))
