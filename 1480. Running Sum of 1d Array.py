# Using for loop
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSumContador = 0
        result = []

        for i in nums:
            runningSumContador += i
            result.append(runningSumContador)

        return result

# Using while loop
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSumContador = 0
        result = []
        i = 0

        while i < len(nums):
            runningSumContador += nums[i]
            result.append(runningSumContador)
            i += 1

        return result