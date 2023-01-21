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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode currNode = head;
        ListNode following = head;
        while(currNode != null) {
            following = following.next;
            currNode.next = prev;
            prev = currNode;
            currNode = following;
        }
        return prev;
    } 

} 

// using recursion 
class Solution {
    public ListNode reverseList(ListNode head) {
         // using recursion 

         if(head == null || head.next == null)
            return head;
        ListNode reversedSubList = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return reversedSubList;

        
    }
}





