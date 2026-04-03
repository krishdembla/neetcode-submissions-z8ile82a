# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head #set curr to the original head
        prev = None #set previous node to none

        while curr:
            temp = curr.next #set the actual original next node to temp
            curr.next = prev #set the current node's next to point to the previous element 
            prev = curr #set previous to the current element
            curr = temp #and set current to temp (next element)
        return prev

            

            


