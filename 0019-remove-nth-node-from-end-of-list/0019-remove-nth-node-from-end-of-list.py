# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        brute force is to first traverse the entire ll to get the length
        then you need to find the diff between total length and n 
        the diff will be the node before the node to be removed. Iterate to that node and then if the node.next is not None then remove it if the node is head then after removing you need to update the head 
        '''
        dummy = ListNode(0,head)
        slow = dummy
        fast = head

        while fast and n > 0:
            fast = fast.next
            n -= 1 
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        
        