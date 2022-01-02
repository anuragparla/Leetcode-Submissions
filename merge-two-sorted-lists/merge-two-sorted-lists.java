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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode l = new ListNode(0);
        ListNode curr = l;
        while (list1 != null || list2 != null) {
            if (list1 == null) {
                if (l.next != null) {
                    curr.next = list2;
                    return l.next;
                }
                else {
                    return list2;
                }
            }
            else if (list2 == null) {
                if (l.next != null) {
                    curr.next = list1;
                    return l.next;
                }
                else {
                    return list1;
                }
            }
            else {
                if (list1.val <= list2.val) {
                    curr.next = new ListNode(list1.val);
                    curr = curr.next;
                    list1 = list1.next;
                }
                else {
                    curr.next = new ListNode(list2.val);
                    curr = curr.next;
                    list2 = list2.next;
                }
            }
        }
        return l.next;
    }
}