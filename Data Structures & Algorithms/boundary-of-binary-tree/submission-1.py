# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        if root.left is None and root.right is None:
            return [root.val]
        
        def isLeaf(node):
           return node is not None and node.left is None and node.right is None

        left = []
        cur = root.left
        while cur: #while a left child exists
            if not isLeaf(cur): #if it is not a leaf, append left to the left boundary
                left.append(cur.val)
            if cur.left: #if the current has a left update current to point to the next left
                cur = cur.left
            else: #this means cur did not have a left so go to its right
                cur = cur.right
        
        cur = root
        leaves = []
        def dfs(cur):
            if cur is None:
                return
            if isLeaf(cur):
                leaves.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        dfs(cur)
        
        cur = root.right
        right = []
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
            
            
            
        
            



        

            