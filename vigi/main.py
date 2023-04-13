def solution(intervals):
    ans = []
    #print(intervals[0])
    s = intervals[0][0]
    e = intervals[0][1]
    index = 1
    while True:
        if index == len(intervals):
            break
        now_s = intervals[index][0]
        now_e = intervals[index][1]

        #print(e)

        if e >= now_s:
            e = max(e, now_e)
            index += 1
            continue
        else:
            #jprint([s, e])
            tmp = ''
            tmp = str(s)+str(e)
            tmp = ','.join(tmp)
            ans.append([tmp])
        
        s = now_s
        e = now_e
        index += 1

    tmp = ''
    tmp = str(s)+str(e)
    tmp = ','.join(tmp)
    #tmp = tmp.replace("'","")
    t = []
    t.append(tmp)
    ans.append(t)
    #print([s, e])
    ans = str(ans).replace("'","")
    return ans


#A = list(map(list, input().split()))
import ast

input_str = input()
input_list = ast.literal_eval(input_str)

#print(input_list)

print(solution(input_list))
