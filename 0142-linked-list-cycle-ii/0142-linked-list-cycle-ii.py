# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isCycle(self,slow,fast):
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return [True, fast]
        return [False, fast]
        
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        cycle = self.isCycle(slow,fast)
        fast = cycle[1]
        if cycle[0]:
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow 
        return None
            
            
                

        


        