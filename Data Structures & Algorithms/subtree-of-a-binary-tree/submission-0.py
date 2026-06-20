class Solution:
    def isSameTree(self, p: Optional[TreeNode],
                   q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True

        if root is None:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))