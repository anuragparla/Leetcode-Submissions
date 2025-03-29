"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
'''
My understanding: 
I need to create a deep copy of the provided Linked List 
What makes this problem challenging is the fact that it has an 
additional random pointer
We can leverage hashMap to map original node to the copied node
Once again iterate through the original linked list and the access its
next and random via the hashMap. The corresponding result would be the 
copied nodes and now I can set the .next and .random for the copied node
Time: O(n)
Space: O(n)
'''
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None : None}

        curr = head 
        # cloning the nodes 
        while curr:
            copy = Node(curr.val) # the copied node will have next and random set to None
            oldToCopy[curr] = copy
            curr = curr.next 
        curr = head 
        # actual deep copy
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]


        