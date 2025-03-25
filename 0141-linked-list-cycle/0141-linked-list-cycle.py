# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        I am assuming i'll use hashmap to keep track of node values and its index 
        if the .next is a value in the hashmap and if it's index is less than the curr 
        index, it means there is a cycle
        return true 
        if the while loop exits then it means there is .next = None which means there 
        is no cycle
        '''
        curr = head
        valueIndexMap = {}
        while curr != None:
            if curr not in valueIndexMap:
                valueIndexMap[curr] = curr
            if curr.next in valueIndexMap:
                return True
            curr = curr.next
        return False

        