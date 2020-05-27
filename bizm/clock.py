class Solution:
    def clock_angle(hour, min):
        ang_h = hour/6*180 + ang_m/180*15
        ang_m = min/30*180
       

diff = abs(ang_h-ang_m)
if diff &gt; 180:
    ans = diff%180
else:
    ans = diff

print(diff)

if __main__ == __init__:
    s = Solution
    s.clock_angle(13, 35)

