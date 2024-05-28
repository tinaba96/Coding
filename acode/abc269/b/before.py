B = 9
for o in range(10):
    A = str(input())
    forB = False
    end = False
    flag = False
    for j in range(len(A)):
        if end == False and flag == False and A[j] == '#':
            AA = o
            C = j
            flag = True

        if end == False and flag == True and A[j] == '.':
            D = j
            end = True

        if A[j] == '#':
            forB = True

    if end == True and forB == False:
        B = o
        break

print(AA+1, B+1)
print(C+1, D+1)







