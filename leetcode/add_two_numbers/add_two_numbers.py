# This is the first medium leetcode problem I have completed successfully without using AI, google search, or my notes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0, None)
        output_head = output
        current1 = l1
        current2 = l2
        carry = 0

        while current1 is not None and current2 is not None:
            node_sum = current1.val + current2.val + carry
            if node_sum >= 10:
                carry = 1
                node_sum = node_sum % 10
            else:
                carry = 0
            output.next = ListNode(node_sum, None)
            current1 = current1.next
            current2 = current2.next
            output = output.next
        
        while current1 is not None:
            # add carry too later
            node_sum = current1.val + 0 + carry
            if node_sum >= 10:
                carry = 1
                node_sum = node_sum % 10
            else:
                carry = 0
            output.next = ListNode(node_sum, None)
            current1 = current1.next
            output = output.next

        while current2 is not None:
            # add carry too later
            node_sum = current2.val + 0 + carry
            if node_sum >= 10:
                carry = 1
                node_sum = node_sum % 10
            else:
                carry = 0
            output.next = ListNode(node_sum, None)
            current2 = current2.next
            output = output.next
        
        if carry >= 1:
            output.next = ListNode(carry, None)
        
        return output_head.next