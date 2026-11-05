# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None):
            return False
        
        alreadySeen = []
        curr = head;

        while (1):
            if (curr.next in alreadySeen):
                return True
            if (curr.next == None):
                return False
            alreadySeen.append(curr)
            curr = curr.next




        # if the current node points to a node we have already visited, then return true
        # if list empty, return null
        # create hash table of ListNode objects
        # while true
            # if  curr->next is in the hash table, return true
            # if curr -> next == null, return false
            # incriment node
            

        



# a -> b -> c -> a 

        