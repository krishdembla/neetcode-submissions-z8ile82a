# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        dummy.next = head
        if not head or not head.next:
            return
        slow = head
        fast = head
        #finding middle point of lists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #separating into two pointers that point to the end of one list and the start of the second list
        second = slow.next
        slow.next = None

        #reversing the second list
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #merging the two
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            #updating
            first = temp1
            second = temp2
        
        return