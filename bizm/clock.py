class Solution:
    def clock_angle(self, hour, minu):
        ang_m = minu/30*180
        ang_h = hour/6*180 + ang_m/180*15
        diff = abs(ang_h-ang_m)
        if diff > 180:
            ans = diff%180
        else:
            ans = diff
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.clock_angle(15, 35))


