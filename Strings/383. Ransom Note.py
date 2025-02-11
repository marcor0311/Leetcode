# Using hash table
# We save the letters in magazine in a hash table
# then we iterate over the letters in ransomNote
#   if the letter is not in the hash table we return False
#   otherwise we decrease the value of the letter in the hash table.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cont = {}

        for letter in magazine:
            cont[letter] = cont.get(letter, 0) + 1
        
        for letter in ransomNote:
            if cont.get(letter, 0) == 0:
                return False
            cont[letter] -=1
        
        return True