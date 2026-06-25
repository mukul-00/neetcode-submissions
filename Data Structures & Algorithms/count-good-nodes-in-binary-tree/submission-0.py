# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
       self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if node is None:
                return
            
            if node.val >= max_so_far:
                self.count += 1
            
            max_so_far = max(max_so_far, node.val)

            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        
        dfs(root, root.val)
        return self.count


        