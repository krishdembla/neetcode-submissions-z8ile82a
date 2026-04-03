
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #if node has right (not right child), set its pointer to that right node else NULL
        #every leaf node will have NULL next
        #we need to modify nexts to get our order through doing a dfs of left first and then right

        def append(cur):
            if cur is None:
                return
            if cur == root:
                cur.next = None

            if cur.left:
                cur.left.next = cur.right
                if cur.next: #if current has a subtree (root doesnt have next)
                    cur.right.next = cur.next.left #linking right's next to the subtrees left or cousin
                append(cur.left)
                append(cur.right)

        append(root)
        return root
        
            