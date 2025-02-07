class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # recordar que en un arreglo la primera posición es 0
        i = 0
        
        # toda lista tendra un indice longitud - 1
        # Ejemplo: [1, 2, 3] -> longitud = 3, indice = 2
        while i < len(nums) - 1:
            # Comparar el elemento actual con el siguiente
            if nums[i] == nums[i+1]:
                # Si son iguales se elimina solo el siguiente
                nums.pop(i + 1)
            else:
                # Sino continuamos con el siguiente elemento
                i += 1
        # Retornamos la longitud del arreglo sin duplicados
        return len(nums)
