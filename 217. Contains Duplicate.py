# Can be more efficient
# Solved using sorting
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        i = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False