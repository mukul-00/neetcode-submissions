# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def __init__(self):
#         self.preorder = 0

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         if root is None:
#             return -1

#         # left
#         leftAns = self.kthSmallest(root.left, k)
#         if leftAns != -1:
#             return leftAns
        
#         # root
#         self.preorder += 1
#         if self.preorder == k:
#             return root.val

#         # right
#         rightAns = self.kthSmallest(root.right, k)
#         if rightAns != -1:
#             return rightAns
        
#         return -1
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[k - 1]
        