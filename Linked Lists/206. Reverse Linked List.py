# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Previous pointer = null
        nodo_previo = None
        # Current pointer -> Head
        nodo_actual = head

        # Until we get to the end of the linked list
        while nodo_actual:

            # Save the next node after the actual node
            next = nodo_actual.next

            # Reverse the pointer of the actual node
            # Before: Actual -> Next (None -> 1 -> 2)
            # After: Actual -> Previous (1 -> None)
            nodo_actual.next = nodo_previo

            # Previous node moves to actual node
            # Actual node moves to next node
            nodo_previo = nodo_actual
            nodo_actual = next

        # Return the last pointer to receive the linked list
        return nodo_previo  