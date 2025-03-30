# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        storageList = []
        curr = head
        while curr:
            storageList.append(curr.val)
            curr = curr.next
        p1 = 0
        p2 = len(storageList)-1
        
        while p1<p2:
            if storageList[p1]!= storageList[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    