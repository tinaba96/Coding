file = open("task1_test_data.input.txt", "r")
line = file.readline()
N = int(line)
filesub = open("output.txt", 'w')
for i in range(N):
    line = file.readline()
    line = file.readline()
    n = int(line)
    awake_time = 0
    sleep_time = 0
    st = {}
    en = {}

    for j in range(n):
        #ans_sleep_hour = 0
        #ans_sleep_hour = 0
        line = file.readline()
        st[j], en[j] = line.split()
        if j > 0:
            if int(en[j-1][0:2]) > int(st[j][0:2]):
                ans_awake_hour = 24 - int(en[j-1][0:2]) + int(st[j][0:2])
            else:
                ans_awake_hour = int(st[j][0:2]) - int(en[j-1][0:2])
            ans_awake_min = int(st[j][3:5]) - int(en[j-1][3:5])
            awake_time += 60*ans_awake_hour+ans_awake_min
        if int(st[j][0:2]) > int(en[j][0:2]):
            ans_sleep_hour = 24 - int(st[j][0:2]) + int(en[j][0:2])
        else:
            ans_sleep_hour = int(en[j][0:2]) - int(st[j][0:2])
        ans_sleep_min = int(en[j][3:5]) - int(st[j][3:5])
        sleep_time += 60*ans_sleep_hour+ans_sleep_min
    filesub.write("Case #"+str(i+1)+": " + str(awake_time) + " " +str(sleep_time)+"\n")

filesub.close()
    
    

