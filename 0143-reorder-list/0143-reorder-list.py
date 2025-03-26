# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        my observations 
        inserting the 2nd half to the 1st 
        how do you determine the mid point? using fast and slow pointers
        we can skip the middle element and iterate the 2nd half from the node 
        next to the middle element 
        """
        #step 1: finding the mid node by using fast n slow 
        fast, slow = head, head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        mid = slow 
        prev = None 
        start = mid.next  # second half beginning
        mid.next = None
        curr = start
        #step 2: reversing 2nd half of the list
        while curr != None: 
            nextNode = curr.next # 5 
            curr.next = prev  # 4 -> None 
            prev = curr # 4 
            curr = nextNode # 5 
         

        
        #step 3: merge the lists
        first_half = head 
        second_half = prev 
        while second_half:
            temp1 = first_half.next 
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1 
            second_half = temp2 
            first_half = temp1 
        
        return head 



       

    
