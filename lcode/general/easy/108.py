# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: []):
    #def sortedArrayToBST(self, nums: []) -> Optional[TreeNode]:
        l = len(nums)
        if l == 1:
            return TreeNode(nums[0])
        m = l//2

        if nums[:m] == []:
            if m+1 < l:
                return TreeNode(nums[m], None, self.sortedArrayToBST(nums[m+1:]))
            else:
                return TreeNode(nums[m], None, None)

        if nums[m:] == []:
            return TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), None)

        if m+1 < l:
            return TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), self.sortedArrayToBST(nums[m+1:]))
        else:
            return TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), None)
        

p = [1,2]
print(p)
print(p[:1])
print(p[1:])



