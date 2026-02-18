# Recursive version

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Not required for this leetcode problem but good guardrail for the future
        if root is None:
            return True

        def compare(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            if left.val != right.val:
                return False
            else:
                return compare(left.left, right.right) and compare(left.right, right.left)
        
        return compare(root.left, root.right)
    
# Iterative version
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Not required for this leetcode problem but good guardrail for the future
        if root is None:
            return True

        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            if left.val != right.val:
                return False
            else:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        
        return True