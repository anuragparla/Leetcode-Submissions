/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 0;
        if(head.next == null) {     //1 n =1;
            return null;
        }
        ListNode curr = head;
        while(curr != null) {  // 1->2  n =2   2-2 = 0 
            count +=1;
            curr = curr.next;
        }
        curr = head;
        int rem = count-n;
        int tempCount = 1;
        if (rem == 0) {
            return head = head.next;
        }
        else {
            while(tempCount<rem) {
                tempCount +=1;
                curr = curr.next;
                
            }
             curr.next = curr.next.next;
            return head;
        }
            
        }
    
    }
