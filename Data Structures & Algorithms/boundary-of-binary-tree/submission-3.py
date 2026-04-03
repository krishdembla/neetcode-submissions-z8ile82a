# Definition for a binary tree node.
# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if not root.right and not root.left:
            return [root.val]
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        
        left = []
        cur = root.left
        while cur:
            if not isLeaf(cur):
                left.append(cur.val)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        leaves = []
        cur = root
        def dfs(node):
            if node is None:
                return
            if isLeaf(node):
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(cur)

        right = []
        cur = root.right
        while cur:
            if not isLeaf(cur):
                right.append(cur.val)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        right_rev = right[::-1]
        
        res = [root.val]
        res.extend(left)
        res.extend(leaves)
        res.extend(right_rev)
        return res
