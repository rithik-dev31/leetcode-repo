// Last updated: 8/12/2026, 11:29:44 AM
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

        ListNode prev=null;
        ListNode cur=head;

        while(cur!=null){
            ListNode next_node=cur.next;
            cur.next=prev;
            prev=cur;
            cur=next_node;
        }


        return prev;
        
    }
}