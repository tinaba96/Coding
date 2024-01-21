from typing import List

class Solution:
    # dp[i][0, 1] -> max amount of money until index i
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0 for _ in range(l+1)] for k in range(2)]
        for i in range(1, l+1):
            # choose
            dp[i][1] = max(dp[i][1], nums[i]+dp[i-1][0])
            # not choose
            dp[i][0] = max(dp[i][0], max(dp[i-1][0], dp[i-1][1]))

            





