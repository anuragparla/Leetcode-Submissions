# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        we need a dummynode so that we'll have a starting point for the 
        merged list. Since the both the lists are in sorted order, we can
        iterate both of them together. I do know their lengths might vary
        Whichever list is remaining can be append at the end to the merged 
        list. Until then keep comparing the node values and based on their
        values, append the smaller one first since it is sorted in non desc-
        ending order 
        Time: O(m + n)
        Space O(m+n)
        '''
        dummyNode = ListNode() #starting point only
        curr = dummyNode # reference from the starting point till end so that we don't mess with starting point

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2

        return dummyNode.next
            
        



            
        


        