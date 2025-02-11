class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Divide and conquer
        # Assume the list is already sorted

        # Positions
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            # found it
            if nums[mid] == target:
                return mid
            # if mid is smaller than target
            # discard left half including mid
            elif nums[mid] < target:
                left = mid + 1
            # if mid is greater than target
            # discard right half including mid
            else:
                right = mid - 1  
        return -1