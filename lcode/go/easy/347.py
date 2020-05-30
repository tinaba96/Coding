import collections as c
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = c.Counter(nums)
        ans = []
        for i in range(k):
            ans.append(freq.most_common()[i][0])
        return ans





        

