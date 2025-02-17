class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Hash table to store the closest number to zero
        hash_closest_number = {}
        # Minimum distance to zero
        min_distance = abs(nums[0])
        
        # The first number is the closest number to zero
        hash_closest_number[min_distance] = nums[0]

        # Iterate through the list of numbers
        for num in nums:
            # Calculate the distance to zero
            distance = abs(num)

            # If the distance is not in the hash table or the number is greater than the number in the hash table
            if distance not in hash_closest_number or num > hash_closest_number[distance]:
                # Update the hash table
                hash_closest_number[distance] = num
            # If the distance is less than the minimum distance
            if distance < min_distance:
                # Update the minimum distance
                min_distance = distance
                
        # Return the closest number to zero
        return hash_closest_number[min_distance]