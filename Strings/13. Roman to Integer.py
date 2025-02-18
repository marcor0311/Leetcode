class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 phases
        # 1. Create a hashmap with the roman numbers as keys and their value as the numeric value
        # 2. Iterate over the string to check the current number and the next number to find out if we need to subtract or add.
        
        romanHashMap = { 'I': 1, 
                         'V': 5, 
                         'X': 10, 
                         'L': 50, 
                         'C': 100, 
                         'D': 500, 
                         'M': 1000 }
        
        # Initialize the previous number and the result
        previuousNumber = 0
        result = 0
        # Reverse the string to iterate from right to left (in roman numbers checking from right to left is easier)
        romans = reversed(s)
        
        for roman in romans:
            currentNumber = romanHashMap[roman]
            # If the current number is greater or equal to the previous number we know we need to add
            if currentNumber >= previuousNumber:
                result += currentNumber
            # If the current number is less than the previous number we know we need to subtract
            else:
                result -= currentNumber
                
            # update the previous number    
            previuousNumber = currentNumber
        
        return result
