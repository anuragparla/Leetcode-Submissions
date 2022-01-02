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
        ListNode l = null;
        ListNode curr = l;
        while (list1 != null && list2 != null) {            
            if(list1.val <= list2.val) {
                if (l == null) {
                l = new ListNode(list1.val);
                curr = l;
                }
                else {
                curr.next = new ListNode(list1.val);
                curr = curr.next;
                }
                list1 = list1.next;
            }
            else { 
                if (l == null) {
                l = new ListNode(list2.val);
                curr = l;
                }
                else {
                curr.next = new ListNode(list2.val);               
                curr = curr.next;
                }
                list2 = list2.next;                
            }
        }
        if (list1 == null && list2 == null) {
            return l;
        }
        else if (list1 == null && list2 != null){
            if (curr == null) {
                return list2;
            }
            else {
                curr.next = list2;
            }
        }
        else { 
            if (curr == null) {
                return list1;
            }
            else {
                curr.next = list1;
            }
        }
            return l;
        }
        
        
    
}