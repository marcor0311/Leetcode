class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # usando sort ordenamos las letras en las palabras
        # se comparan todas las letras de las palabras
        if sorted(s) == sorted(t):
            return True
        else:
            return False