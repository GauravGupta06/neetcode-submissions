# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create beforeHead node
        # create curr node, set to beforeHead
        # while both nodes are not null 
        #   compare value between both nodes. 
        #   set curr next to the smaller node
        #   incriment the pointer for the smaller node. 

        # if list1 is not empty then add it to curr next
        # if list2 is not empty than add it to curr next

        # return beforeHead next

        beforeHead = ListNode()
        curr = beforeHead

        while (list1 != None and list2 != None):
        
            if (list1.val <= list2.val):
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        

        if (list1 != None):
            curr.next = list1
    
        elif (list2 != None):
            curr.next = list2
        
        return beforeHead.next

      


        
        




