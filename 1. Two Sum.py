class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        # brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                # si las posiciones no son iguales y la suma de los valores es igual al target
                # entonces retornamos los indices 
                if(i != j and nums[i] + nums[j] == target):
                    return[i,j]
        return []