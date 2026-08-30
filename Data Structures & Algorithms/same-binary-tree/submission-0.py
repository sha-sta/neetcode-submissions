# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        if not p or not q:
            return not p and not q
        if p.val != q.val:
            return False
            
        right = self.isSameTree(p.right, q.right)
        left = self.isSameTree(p.left, q.left)
        
        return right and left
        