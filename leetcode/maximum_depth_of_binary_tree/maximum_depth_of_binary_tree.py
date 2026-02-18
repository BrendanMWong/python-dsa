# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def check(node):
            if node is None:
                # Return node depth, empty node depth = 0
                return 0
            # Return the largest depth of the left and right nodes, but add 1 each time
            return 1 + max(check(node.left), check(node.right))
        
        return check(root)