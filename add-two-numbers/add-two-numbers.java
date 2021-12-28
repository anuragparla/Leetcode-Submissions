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
    /*
    private static long ListToInt(ListNode list) {
        long sum = 0;
        long product = 1;
        ListNode curr  = list; 
        while (curr != null) {
            sum = sum + curr.val * product;
            //System.out.println("sum is " +sum);
            
            product *= 10;
            //System.out.println("prod is" +product);
            curr = curr.next;
        }
        return sum;
        
    }
    
    private static ListNode intToList(long totalSum) {
        ListNode curr = null;
        ListNode head = null;
        long rem = 0;
        while (totalSum != 0) {
            rem = totalSum % 10;
            if (head == null) {
                head = new ListNode ((int)rem);
                curr = head;
            }
            else {
                curr.next = new ListNode((int)rem);
                curr = curr.next;
            }
            totalSum = totalSum/10;
        }
        return head;
    }*/
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        /*
        long resultantSum = 0;
        long sum1 = ListToInt(l1);
        long sum2 = ListToInt(l2);
        System.out.println(sum1);
        System.out.println(sum2);
        resultantSum = ListToInt(l1) + ListToInt(l2); // sum of 2 lists 
        System.out.println(resultantSum);
        //return null;*/
        ListNode curr1 = l1;
        ListNode curr2 = l2; 
        int sum = 0;
        int carry = 0;
        int newNodeVal = 0;
        ListNode newCurr = null;
        ListNode head = null;
        while ((curr1 != null) && (curr2 != null)) {
            sum = curr1.val + curr2.val + carry;
            carry = sum/10;
            newNodeVal = sum%10;
            
            if (head == null) {
                newCurr = head = new ListNode(newNodeVal);
            }
            else {
                newCurr.next = new ListNode(newNodeVal);
                newCurr = newCurr.next;
            }
            curr1 = curr1.next;
            curr2 = curr2.next;
        }
        if(curr1 == null) {
            while(curr2 != null) {
            sum =  curr2.val + carry;
            carry = sum/10;
            newNodeVal = sum%10;
            newCurr.next = new ListNode(newNodeVal);
            newCurr = newCurr.next;
            //curr1 = curr1.next;
            curr2 = curr2.next;      
                }
            
        }
        else {
            while(curr1 != null) {
                
            sum =  curr1.val + carry;
            carry = sum/10;
            newNodeVal = sum%10;
            newCurr.next = new ListNode(newNodeVal);
            newCurr = newCurr.next;
            curr1 = curr1.next;
            //curr2 = curr2.next;      
                
            }
        }
        if (carry != 0) {
            newNodeVal = carry;
            newCurr.next = new ListNode(newNodeVal);
        }
        return head;
    }
}