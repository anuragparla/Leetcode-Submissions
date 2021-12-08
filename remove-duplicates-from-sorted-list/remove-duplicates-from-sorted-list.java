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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode currentNode = head;
        ListNode nextDistinctNode;
        while(currentNode != null) {
            nextDistinctNode = currentNode.next;
            while(nextDistinctNode != null && currentNode.val == nextDistinctNode.val) {
                nextDistinctNode = nextDistinctNode.next;
            }
            currentNode.next = nextDistinctNode;
            currentNode = nextDistinctNode;
        }
        return head;
    }
}