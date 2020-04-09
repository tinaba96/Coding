#104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        for ele in root:
'''
'''
#DFS and Recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

#Iteration
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth
#上は深さ優先探索
'''                 

#BFS
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        q.append((1, root))
        depth = 0
        
        while len(q) > 0:
            current_depth, root = q.popleft()
            if root is not None:
                depth = max(depth, current_depth)
                q.append((current_depth+1, root.left))
                q.append((current_depth+1, root.right))
        return depth
#ok

#572
    def isSubtree(self, s:TreeNode, t:TreeNode) -> bool:
        flag = False
        qs = []
        qt = []
        qs.append(s)
        qt.append(t)

        while len(qs) > 0:
            current = qs.pop()
            if current == qt[0] :
                qt.pop()
                flag = True
                qt.append(t.left)
                qt.append(t.right)
            else:
                flag = False
                qt = []
                qt.append(t)
            qs.append(s.left)
            qs.append(s.right)
            if qs == [] and qt == []:
                break

        if flag == True and t.right == None and t.left == None:
            return True
        else:
            return False



if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(3, 9, 20, null, null, 15, 7))


