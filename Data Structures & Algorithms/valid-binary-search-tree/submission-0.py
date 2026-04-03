# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def valid(node, low, high):
            if node is None:
                return True
            if node.val > low and node.val < high:
                return valid(node.left, low, node.val) and valid(node.right, node.val, high)
            else:
                return False
            return True

        node = root
        return valid(node, float('-inf'), float('inf'))