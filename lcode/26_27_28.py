
class Solution():
    #sorted array
    def removeDuplicates(self, nums: [int]) -> int:
        i = 0
        while i<(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                #print(nums[i], end = "")
                print(nums[i])
                i += 1 

    def removeElement(self, nums: [int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
            '''
            for i in range(len(needle)):
                for j in range(len(haystack)):
                    if needle[i] == haystack[j]:
            '''
        else:
            return -1

#Solution.removeDuplicates(None, [1, 1, 2, 3, 3, 3, 3, 4, 4, 5])
#print(Solution.removeElement(None, [1, 1, 2, 3, 3, 3, 3, 4, 4, 5], 4))
print(Solution.strStr(None, "hello", "ll"))


