#[4,2,7,1,3,6,9]
#[4,7,2,9,6,3,1]


# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def depth(root):
            if not root:
                return 0
            root.left, root.right = root.right, root.left
            depth(root.left)
            depth(root.right)

        depth(root)
        return root
        


