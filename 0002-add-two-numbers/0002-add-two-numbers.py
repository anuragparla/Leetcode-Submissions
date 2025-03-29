# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        my understanding:
        I know the input is non negetive and non empty i.e. there will be no empty list
        Also no leading zero
        the numbers are arranged in reverse order which makes it easy to add and pass the carry over
        iterate through the loops together
        if one of them ends early, then consider the value after none is 0. this will help to continue
        traversing through the other loop 
        sum = l1.val + l2.val + carryOver 
        carryOver is calculated as sum // 10 
        val to be added to the resulting node is sum % 10 
        '''
        dummyNode = ListNode()
        curr = dummyNode 
        carryOver = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0                          
            val2 = l2.val if l2 else 0 
            sum = val1 + val2 + carryOver
            carryOver = sum // 10 
            resultingDigit = sum % 10
            curr.next = ListNode(resultingDigit)
            curr = curr.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        if carryOver > 0:
            curr.next = ListNode(carryOver)
        return dummyNode.next 
# 1 
# 9 9 9 
# 1 + 9 sum = 10 c = 1     ->0->
# 0 + 9 + 1 = 10 c = 1     ->0->0->
# 0 + 9 + 1 = 10 c = 1     -> 0 -> 0 -> 0 



      

       

        