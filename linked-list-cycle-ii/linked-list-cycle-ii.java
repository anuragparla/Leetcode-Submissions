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
    private ListNode getIntersection(ListNode head) {
        ListNode slowPtr = head;
        ListNode fastPtr = head;
        
        while(fastPtr != null && fastPtr.next != null) {
            fastPtr = fastPtr.next.next;
            slowPtr = slowPtr.next;
            if(fastPtr == slowPtr) return fastPtr;
        }
        return null;
    }
    public ListNode detectCycle(ListNode head) {
       
        if( head == null) return null;
        ListNode intersectionPtr = getIntersection( head);
        if(intersectionPtr == null) return null;
        
        while(head != intersectionPtr) {
            head = head.next;
            intersectionPtr = intersectionPtr.next;
        }
        return head;
    }
}