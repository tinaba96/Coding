Q = int(input())

bug = {}
tmp = 0
m = 10010010001001000100

for q in range(Q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        m = min(m, x[i])
        bug[x[1]] += 1
        #bug.append(x[1])

    if x[0] == 2:
        tmp += x[1]
    if x[0] == 3:
        #index, m = min(enumerate(bug), key = lambda x:x[1])
        print(min(bug[0])+tmp)
        if bug[min(bug)] !=0:
            bug[min(bug)] -= 1
        else:
            del bug[min(bug)]
            bug[min(bug)] -= 1

        #bug.remove(min(bug))
        #bug.pop(bug[index])




