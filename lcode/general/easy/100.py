# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
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



	







        


