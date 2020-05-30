class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, i: int, j: int) -> int:
        tot = sum(self.arr[i:j+1])
        return tot
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
