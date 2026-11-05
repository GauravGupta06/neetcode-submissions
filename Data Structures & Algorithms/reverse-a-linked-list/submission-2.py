# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # to make sure we have atleast 2 node
        if (head == None or head.next == None):
            return head

        previous = head
        curr = head.next
        previous.next = None
        Next = None

        while (curr != None):
            Next = curr.next
            curr.next = previous 
            previous = curr
            curr = Next

        head = previous
        return head

# [] -> [] ->[] ->[] -> 



        