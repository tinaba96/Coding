#要復習

#Definition for a binary tree node.
class TreeNode:
 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        cnt = 0
        ans = 0


        def count(node1, cnt):
            if not node.left:
                return cnt
            else:
                count(node.left, cnt+1)
            if not node.right:
                return cnt
            else:
                count(node.right, cnt+1)


        ans = max(count(root.left) + count(root.right))

'''

#ans
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

#self.amsのようにselfを使わないと、diameterOfBinaryTree関数の中にあるdepth関数で用いる変数ansが定義されていないことになってしまう。


if __name__ == '__main__':
    s = Solution()
    #print(TreeNode(val=2).val)
    '''
    TreeNode(val=1).left = TreeNode(val=2)
    TreeNode(val=1).right = TreeNode(val=3)
    TreeNode(val=2).left = TreeNode(val=4)
    TreeNode(val=2).right = TreeNode(val=5)
    '''
    print(s.diameterOfBinaryTree(TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3))))





        
