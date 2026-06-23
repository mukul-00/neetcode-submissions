# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def __init__ (self):
#         self.ans = 0

#     def height(self, node):
#         if(node == None):
#             return 0
#         lh = self.height(node.left)
#         rh = self.height(node.right)
#         return max(lh, rh) + 1

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

#         if(root == None):
#             return 0
#         lh = self.height(root.left)
#         rh = self.height(root.right)
#         diameter = lh + rh
#         self.ans = max(diameter, self.ans)
#         self.diameterOfBinaryTree(root.left)
#         self.diameterOfBinaryTree(root.right)

#         return self.ans

class Solution:
    def __init__ (self):
        self.ans = 0

    def height(self, node):
        if(node == None):
            return 0
        lh = self.height(node.left)
        rh = self.height(node.right)

        diameter = lh + rh

        self.ans = max(diameter, self.ans)

        return max(lh, rh) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.height(root)

        return self.ans


 