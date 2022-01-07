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
import java.util.Random;
class Solution {
        ListNode head;
        ListNode curr;
        int size = 0;
    
    private int getSize(ListNode head) {
         curr = head;
        int n = 0;    
        while(curr.next != null) {
            curr = curr.next;
            n +=1;
        }
        return n;
    }    
    
    public Solution(ListNode head) {
        this.head = head;
        this.curr = head;
        size = getSize(this.head);
        
    }
    
    public int getRandom() {
        
        Random rand = new Random();
        int res;
        int counter = 0;
        res = rand.nextInt(size+1);
        curr = head;
        while(counter<res) {   
            curr = curr.next;
            counter +=1;
        }
        return curr.val ;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */