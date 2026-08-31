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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int[] result = {-1, -1};

        if (head == null || head.next == null || head.next.next == null){
            return result;
        }

        ListNode prev = head;
        ListNode curr = head.next;
        int index = 1;
        int firstCrit = -1;
        int lastCrit = -1;
        int minDist = Integer.MAX_VALUE;

        while (curr.next != null) {
            ListNode nextNode = curr.next;

            if ((curr.val > prev.val && curr.val > nextNode.val)|| (curr.val < prev.val && curr.val < nextNode.val)){

                if (firstCrit == -1){
                    firstCrit = index;
                }else {
                    minDist = Math.min(minDist, index - lastCrit);
                }
                lastCrit = index;
                
            }

            prev = curr;
            curr = nextNode;
            index++;
        }

        if (minDist != Integer.MAX_VALUE) {
            result[0] = minDist;
            result[1] = lastCrit - firstCrit;
        }

        return result;
        
    }
}