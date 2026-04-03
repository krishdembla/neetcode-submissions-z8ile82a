# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0 #to store length of linkedlist
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        removeIdx = N - n #we need to remove nth idx from right so that is the N - n idx from left
        if removeIdx == 0: #if the idx to remove is the head
            return head.next
        
        curr = head
        for i in range(N - 1): #iterate thru len of linked list
            if (i + 1) == removeIdx: #i + 1 because iteration starts from 0 but the nth idx starts counting from 1
                curr.next = curr.next.next #set currents next pointer to skip the next and point to next of next
                break
            curr = curr.next #if removeIdx not found we continue iterating
        return head