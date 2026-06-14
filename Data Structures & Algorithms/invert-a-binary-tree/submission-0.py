# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#=================== DFS =========================================
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root == None:
#             return None
        
#         root.left. root.right = root.right, root.left

#         invertTree(root.left)
#         invertTree(root.right)

#         return root

#=================== BFS =========================================

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        q = deque([root])

        while q:

            temp = q.popleft()

            temp.left, temp.right = temp.right, temp.left

            if temp.left:
                q.append(temp.left)
            
            if temp.right:
                q.append(temp.right)
        
        return root