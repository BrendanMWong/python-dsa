# Recursive version, function inside a function

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(node):
            if node is None:
                return
            # Call left first
            dfs(node.left)
            # Record this node second
            output.append(node.val)
            # Call right third
            dfs(node.right)
        
        dfs(root)
        return output

# Iterative version, using a stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        current = root

        while current or stack:

            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()
            output.append(current.val)

            # Go right next
            current = current.right

        return output
