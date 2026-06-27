class Solution:
    def buildTree(self, preorder, inorder):
        self.pre_idx = 0

        def search(left, right, val):
            for i in range(left, right + 1):
                if inorder[i] == val:
                    return i
            return -1

        def dfs(left, right):
            if left > right:
                return None

            root = TreeNode(preorder[self.pre_idx])

            mid = search(left, right, root.val)
            self.pre_idx += 1

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)