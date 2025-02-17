class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # save the result in a list
        result = []
        
        i = 0

        # iteration while i is less than the length of word1 or word2
        while i < len(word1) or i < len(word2):
            # if i is less than the length of word1 we add the letter at index i to the result
            if i < len(word1):
                result.append(word1[i])
            # if i is less than the length of word2 we add the letter at index i to the result
            if i < len(word2):
                result.append(word2[i])
            # keep going until we iterate over all the letters in word1 and word2
            i += 1
        # return the result as a string
        return ''.join(result)
    
# How does this include the edge cases?

# Note: Loop does all the work; when one word is longer then when the shorter word is done
#       the loop will continue to add the remaining letters of the longer word to the result.
        