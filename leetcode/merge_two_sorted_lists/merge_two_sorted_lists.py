# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize dummy head and pointer
        # Purpose: to avoid a special case, comparing the first node of list1 and list2
        dummyheadnode = ListNode(0, None)
        dummypointer = dummyheadnode

        # Initialize pointers for list1 and list2
        list1pointer = list1
        list2pointer = list2

        # Build output list based on value comparisons between list1 and list2
        while list1pointer is not None and list2pointer is not None:
            if list1pointer.val <= list2pointer.val:
                # Set list1's pointer as dummy list's next node
                dummypointer.next = list1pointer

                # Increment the pointers
                dummypointer = dummypointer.next
                list1pointer = list1pointer.next
            else:
                # Set list2's pointer as dummy list's next node
                dummypointer.next = list2pointer

                # Increment the pointers
                dummypointer = dummypointer.next
                list2pointer = list2pointer.next
        
        # Attach leftovers in the non empty list
        while list1pointer is not None:
            dummypointer.next = list1pointer
            dummypointer = dummypointer.next
            list1pointer = list1pointer.next
        while list2pointer is not None:
            dummypointer.next = list2pointer
            dummypointer = dummypointer.next
            list2pointer = list2pointer.next

        # Return all nodes after dummy head node
        return dummyheadnode.next
        