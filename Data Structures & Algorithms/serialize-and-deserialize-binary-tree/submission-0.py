# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        result = []

        q = deque([root])

        while q:
            temp = q.popleft()

            if temp != None:
                result.append(str(temp.val))
                q.append(temp.left)
                q.append(temp.right)
            else:
                result.append("null")
        
        return ",".join(result)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "":
            return None

        values = data.split(",")

        root = TreeNode(int(values[0]))
        q = deque([root])

        i = 1

        while q:
            temp = q.popleft()

            if values[i] != "null":
                temp.left = TreeNode(int(values[i]))
                q.append(temp.left)
            i += 1

            if values[i] != "null":
                temp.right = TreeNode(int(values[i]))
                q.append(temp.right)
            i += 1
        
        return root




