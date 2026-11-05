# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None):
            return list2
        
        curr1 = list1 
        curr2 = list2
        dummy = returnNode = ListNode(0, None)

        while (curr1 != None and curr2 != None):
            if (curr1.val <= curr2.val):
                returnNode.next = curr1
                returnNode = returnNode.next
                curr1 = curr1.next
            else:
                returnNode.next = curr2
                returnNode = returnNode.next
                curr2 = curr2.next

        if (curr1 != None):
            returnNode.next = curr1
            
        if (curr2 != None):
            returnNode.next = curr2

        return dummy.next
        




