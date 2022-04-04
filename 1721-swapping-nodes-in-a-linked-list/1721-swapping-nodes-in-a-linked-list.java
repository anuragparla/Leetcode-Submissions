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
    public ListNode swapNodes(ListNode head, int k) {
        int n = 0;
        ListNode curr = head;
        int lc = 1;
        while (curr != null) {
            n +=1;
            curr = curr.next;
        }
        curr = head;
        ListNode leftNodeAddr = null;
        ListNode rightNodeAddr = null;
        while(curr != null && lc<=k-1){
            lc +=1;
            curr = curr.next;
        }
        leftNodeAddr = curr;
        
        ListNode newCurr = head;
        int rc = n-k;
        lc = 1;
        while(newCurr != null && lc<=rc){
            lc +=1;
            newCurr = newCurr.next;
        }
        rightNodeAddr = newCurr;
        System.out.println("left node"+leftNodeAddr.val);
        System.out.println("right node"+rightNodeAddr.val);
        
        int temp = leftNodeAddr.val;
        leftNodeAddr.val = rightNodeAddr.val;
        rightNodeAddr.val = temp;
        
        return head;
    }
}