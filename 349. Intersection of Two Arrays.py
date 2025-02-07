class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        
        # recorremos toda la lista 1
        for i in nums1:
            # 1. si el elemento no se encuentra en la lista de interseccion 
            # 2. y el elemento si se encuentra en la lista 2
            # entonces lo agregamos a la lista de interseccion
            if i not in intersection and i in nums2:
                intersection.append(i)
                
        return intersection