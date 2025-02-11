# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Upper number is a reference to acarreo
        
        upper_number = 0
        result = []

        while l1 is not None or l2 is not None or upper_number != 0:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            total = num1 + num2 + upper_number

            # to obtain first numer aka upper_number
            upper_number = total // 10

            # to add last digit
            result.append(total%10)

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        head = ListNode(result[0])
        actual = head
        for val in result[1:]:
            actual.next = ListNode(val)
            actual = actual.next

        return head

        