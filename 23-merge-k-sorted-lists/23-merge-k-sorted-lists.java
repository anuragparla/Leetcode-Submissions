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
    public ListNode merge(ListNode[] lists,int l,int r){
        if(l==r)
            return lists[l];
        
        int mid=l+(r-l)/2;
        
        ListNode left=merge(lists,l,mid);
        ListNode right=merge(lists,mid+1,r);
        return mergeLinkedList(left,right);
    }
    public ListNode mergeLinkedList(ListNode head1,ListNode head2){
        ListNode newHead,ptr;
        
        if(head1==null){
            return head2;
        }
        else if(head2==null){
            return head1;
        }
        
        if(head1.val>head2.val){
            newHead=head2;
            head2=head2.next;
        }
        else
        {
            newHead=head1;
            head1=head1.next;
        }
        
        ptr=newHead;
        
        while(head1!=null && head2!=null){
            if(head1.val>head2.val){
                ptr.next=head2;
                head2=head2.next;
                ptr=ptr.next;
            }
            else{
                ptr.next=head1;
                head1=head1.next;
                ptr=ptr.next;
            }
        }
        
        if(head1!=null){
            ptr.next=head1;
        }
        else if(head2!=null){
            ptr.next=head2;
        }
        
        return newHead;
    }
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length==0)
            return null;
        
        return merge(lists,0,lists.length-1);
    
    }
}