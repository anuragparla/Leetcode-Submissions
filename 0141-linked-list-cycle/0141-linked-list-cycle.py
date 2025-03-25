# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        I am assuming i'll use hashmap to keep track of node
        if the .next is a value in the hashmap
         it means there is a cycle
        return true 
        if the while loop exits then it means there is .next = None which means there 
        is no cycle
        Time: O(n)
        Space: O(n)
        '''
        # curr = head
        # valueIndexMap = {}
        # while curr != None:
        #     if curr not in valueIndexMap:
        #         valueIndexMap[curr] = curr
        #     if curr.next in valueIndexMap:
        #         return True
        #     curr = curr.next
        # return False


        '''
        Improved solution: Flyod Marhsall's algorithm also called hare and tortoise
        Time: O(n)
        Space: O(1)
        slow and fast pointers. slow moves by 1 and fast moves by two. 
        if both meet then its a cycle but if fast reaches none then no cycle 
        '''
        fast, slow = head, head 
        while fast !=None and slow != None:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return False
            else:
                fast = fast.next
            if fast == slow:
                return True 
        return False 
            


        