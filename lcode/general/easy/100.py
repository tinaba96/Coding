# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
'''
class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution(object):
	def isSameTree(self, p, q):
		"""
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if trace(p,q):
			return True
		else:
			return False

	def trace(self, p, q):
		if p.v != q.v or p.right.val != q.right.val or p.left.val != q.left.val:
			return False
		if p.left and q.left:
			if !trance(q.left, q.left):
				return False
		if p.right and q.right:
			if !trance(q.right, q.right):
				return False
		return True



	
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False
            return check(p.left, q.left) and check(p.right, q.right)
        return check(p, q)

def build_tree_from_list(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while i < len(vals):
        current = queue.pop(0)
        if vals[i] is not None:
            current.left = TreeNode(vals[i])
            queue.append(current.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            current.right = TreeNode(vals[i])
            queue.append(current.right)
        i += 1
    return root

# Input arrays
p_list = [1, 2]
q_list = [1, None, 2]

# Convert arrays to binary trees
p_tree = build_tree_from_list(p_list)
q_tree = build_tree_from_list(q_list)

# Create an instance of Solution and use isSameTree
sol = Solution()
result = sol.isSameTree(p_tree, q_tree)
print(result)  # Output: False






        


