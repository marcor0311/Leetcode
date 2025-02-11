# Using for loop
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest_amount = 0
        for customer in accounts:
            richest_amount = max(richest_amount, sum(customer))
        return richest_amount