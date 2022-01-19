/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        
        
         if (head == null || head.next == null) {
            return null;
        }
        else {
            ListNode hare = head;
            ListNode tortoise = head;
            ListNode entry = head;
            
            while(hare.next != null && hare.next.next != null) {
                    // here the fast and slow pointers should be first moved
                    // else since fast and slow are initalized to head at starting
                    // checking that condition at first would lead to error
                    tortoise = tortoise.next;
                    hare = hare.next.next;
                if(hare == tortoise) {
                    ListNode temp = tortoise;
                   
                    while(entry != temp)
                    {
                        temp = temp.next;
                        entry = entry.next;
                    }
                    return entry;
                }
            }
            return null;
        }
    }
}