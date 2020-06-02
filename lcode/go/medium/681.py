class Solution:
    def nextClosestTime(self, time: str) -> str:
        time.replace(":", "")
        elem = []
        for ele in time:
            elem.append(int(ele))
        elem.sort()
        for ele in time:
            if ele > time[4]:
                return time[0]+time[1]+":"+time[3]+ele

        if max(elem) < time[4]:
            return time[0]+time[1]+":"+elem[1+elem.index(time[3])]+elem[0]

        h = int(time[0]+time[1])
        diff = 24
        flag = False

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




                    





        








        




