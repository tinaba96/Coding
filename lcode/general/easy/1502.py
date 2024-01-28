from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int])-> bool:
        sortedList = sorted(arr)
        base = sortedList[1] - sortedList[0]
        ans = True
        for i in range(len(sortedList)-1):
            if sortedList[i+1]-sortedList[i] != base:
                ans = False
        return ans


print(Solution().canMakeArithmeticProgression([4, 2, 1]))

