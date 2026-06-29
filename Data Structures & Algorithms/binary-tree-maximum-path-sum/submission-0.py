# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDownPath(self, node):
        if node is None:
            return 0
        
        left = max(0, self.maxDownPath(node.left)) # why 0, maxdow.. -> bcz if node is -ve then return 0
        right = max(0, self.maxDownPath(node.right))

        self.maxi = max(self.maxi, left + right + node.val)

        return node.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        self.maxDownPath(root)
        return self.maxi
        
    
#     maxDownPath(1)
# │
# ├── maxDownPath(2)
# │      │
# │      ├── maxDownPath(None) → 0
# │      └── maxDownPath(None) → 0
# │
# │      left = 0
# │      right = 0
# │      self.maxi = 2
# │      return 2
# │
# ├── maxDownPath(3)
# │      │
# │      ├── maxDownPath(None) → 0
# │      └── maxDownPath(None) → 0
# │
# │      left = 0
# │      right = 0
# │      self.maxi = 3
# │      return 3
# │
# left = 2
# right = 3

# self.maxi = 6

# return 4