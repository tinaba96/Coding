
class Solution:
    def nextClosestTime(self, time: str) -> str:
        time = time.replace(':', '')
        elem = []
        for ele in time:
            elem.append(ele)
        elem.sort()
        print(elem)
        for ele in elem:
            if ele > time[3]:
                return time[0]+time[1]+":"+time[2]+ele
        print(elem)
        if max(elem) <= time[3]:
            for ele in elem:
                     if int(ele) <= 5 and ele > time[2]:
                        return time[0]+time[1]+":"+ele+elem[0]

        h = int(time[0]+time[1])
        diff = 24
        flag = False
        s = 0
        t = 0

        for i in range(4):
            for j in range(4):
                if int(elem[i] + elem[j]) <= 24 and int(elem[i] + elem[j]) > h:
                    if diff > abs(h-int(elem[i]+elem[j])):
                        diff = abs(h-int(elem[i]+elem[j]))
                        s = i
                        t = j
                flag = True


        if flag == False:
            return elem[0]+elem[0]+":"+elem[0]+elem[0]
        else:
            return elem[s]+elem[t]+":"+elem[0]+elem[0]



#ans
class Solution(object):
    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

#anotherans
class Solution(object):
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))




        




