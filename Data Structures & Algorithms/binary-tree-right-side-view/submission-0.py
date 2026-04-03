# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #my idea is to use BFS to maintain a level order traversal and keep appending the last element of each level
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop() #pop right most element
                level.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            ans.append(level[-1]) #append first ele since right got popped first
        return ans