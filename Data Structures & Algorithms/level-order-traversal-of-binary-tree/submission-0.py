from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q = deque([root])

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                temp = q.popleft()
                level.append(temp.val)

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right)

            res.append(level)

        return res