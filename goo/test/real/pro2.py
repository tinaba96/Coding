file = open("task2-test-input.txt", "r")
filesub = open("output2.txt", 'w')
line = file.readline()
A = int(line)

def check(j, ele, time, ma):
    ma = max(time, ma) 
    maxi.append(ma)
    for k in range(M):
        if after[j] == before[k]:
            check(k, before[k], time+1, ma)

for i in range(A):
    line = file.readline()
    line = file.readline()
    N, M = map(int, line.split())
    before = []
    after = []
    maxi = []

    for j in range(M):
        line = file.readline()
        left, right = map(int, line.split())
        before.append(left)
        after.append(right)

    for j in range(M):
        ma = 1
        time = 1
        check(j, before[j], time, ma)

    if maxi != []:
        ans = max(maxi)+1
    else:
        ans = 1

    filesub.write("Case #"+str(i+1)+": " + str(ans) + "\n")

filesub.close()
file.close

