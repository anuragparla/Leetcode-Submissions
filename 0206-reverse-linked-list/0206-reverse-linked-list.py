# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        curr = head 

        while curr != None:
            next_node = curr.next
            curr.next = dummyNode.next
            dummyNode.next = curr
            curr = next_node 
        return dummyNode.next

        