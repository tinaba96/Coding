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
        stack_s = []
        stack_t = []
        stack_s.append(s)
        stack_t.append(t)

        while len(stack_s) > 0:
            current_s = stack_s.pop()
            if current_s == stack_t.pop() :
                current_t = current_s
                flag = True
                if current_t.left != None:
                    stack_t.append(current_t.left)
                if current_t.right != None:
                    stack_t.append(current_t.right)
                if current_t.left == None and current_t.right == None:
                    return True
            else:
                flag = False
                stack_t = []
                stack_t.append(t)
            if current_s.left != None:
                stack_s.append(current_s.left)
            if current_s.right != None:
                stack_s.append(current_s.right)

        if flag == True:
            return True
        else:
            return False

    #ans
    def isSubtree(self, s:TreeNode, t:TreeNode) -> bool:
        a = []
        self.preorder(s, a)
        b = []
        self.preorder(t, b)
        a = ''.join(a)
        b = ''.join(b)
    
        if b in a:
            return True
        else:
            return False

    def preorder(self, node, l):
        if not node:
            l.append("#")
            return

        l.append(':'+str(node.val))
        self.preorder(node.left, l)
        self.preorder(node.right, l)

    def isSubtree(self, s: TreeNode, t:TreeNode) -> bool:
        return self.dfs(s, t)

    def dfs(self, node1, node2):
        if not model:
            return False

        if node1.val == node2.val:
            if self.check(node1, node2):
                return True
        if self.dfs(node1.left, node2):
            return True
        if self.dfs(node1.right, node2):
            return True

        return False

    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        return self.check(node1.left, node2.left) and self.check(node1.right, node2.right)

    import collections
    def majorityElement(self, nums: list[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common()[0][0]

    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]


if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth(3, 9, 20, null, null, 15, 7))


