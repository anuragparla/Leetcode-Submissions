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
    public boolean hasCycle(ListNode head) {
        ListNode fp = head;
        ListNode sp;
        if(head == null||head.next == null)  return false;
        sp = fp.next.next;
        while(sp != null){    // 3, 2, 0, -4 pos = 1  2, 0| 0, 2 | -4, 2 | 2 2 
            if(fp == sp) return true;
            fp = fp.next;
            //sp = fp.next != null ? fp.next.next : null;
            sp = sp.next !=null ? sp.next.next : null;
        }
        return false;
    }
}