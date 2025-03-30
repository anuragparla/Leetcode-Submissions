# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # storageList = []
        # curr = head
        # while curr:
        #     storageList.append(curr.val)
        #     curr = curr.next
        # p1 = 0
        # p2 = len(storageList)-1
        
        # while p1<p2:
        #     if storageList[p1]!= storageList[p2]:
        #         return False
        #     p1 += 1
        #     p2 -= 1
        # return True

        '''
        Follow up: Can you do in O(1) space and O(n) time? 
        1 -> 2 -> 3 -> 2 -> 1 
        mid is 3 
        we reverse after mid = 1 - 2 - 3 - 1 - 2 
        before = head 
        after = mid.next 
        before and after not equal then they are not palindrome 
        '''
        #finding mid 
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow 

        #reverse all the nodes after mid 
        secondHalf = mid
        prev = None 
        curr = secondHalf     
        while curr:                     
            nextNode = curr.next     
            curr.next = prev         
            prev = curr             
            curr = nextNode         
        secondHalf = prev 

        #iterate through 2nd half and compare with the 1st half 
        curr = head 
        while secondHalf:
            if curr.val != secondHalf.val:
                return False
            curr = curr.next 
            secondHalf = secondHalf.next
       
        return True
        
        
             

    