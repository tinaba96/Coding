class Solution:
    def clock_angle(self, hour, minu):
        ang_m = (minu/30*180)%360
        print('ag_m:', ang_m)
        ang_h = (hour/6*180 + ang_m/180*15)%360
        print('ag_h:', ang_h)
        diff = abs(ang_h-ang_m)
        print('diff:', diff)
        if diff > 180:
            ans = 360 - diff
        else:
            ans = diff
        return ans

if __name__ == '__main__':
    s = Solution()
    print('15:35 -> ', s.clock_angle(15, 35))
    #102.5
    print('12:5 -> ', s.clock_angle(12, 5))
    #27.5
    print('18:30 -> ', s.clock_angle(18, 30))
    #15.0
    print('23:55 -> ', s.clock_angle(23, 55))
    #27.5
    print('22:13 -> ', s.clock_angle(22, 13))
    #131.5
    print('9:51 -> ', s.clock_angle(9, 51))
    #10.5
    print('4:6 -> ', s.clock_angle(4, 6))
    #87.0
    print('1:50 -> ', s.clock_angle(1, 50))
    #105.0


