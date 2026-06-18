# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root):
        if root is None:
            return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        diff = abs(self.height(root.left) - self.height(root.right)) <= 1

        return left and right and diff