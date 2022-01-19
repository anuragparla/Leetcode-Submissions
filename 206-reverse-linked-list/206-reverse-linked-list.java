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
        ListNode following = head;  // this is given only when the LL can be empty
        while(currNode != null) {
            following = following.next;
            currNode.next = prev;
            prev = currNode;
            currNode = following;
        }
        return prev;
    }
}