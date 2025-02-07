class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split divide la cadena en palabras
        # Se puede representar como:
        # "Batman es el caballero de la Noche" 
        # Eso se guarda como 
        #       ["Batman", "es", "el", "caballero", "de", "la", "Noche"]
        palabras = s.split()

        # Luego se usa reverse para invertir el orden de las palabras
        #       ["Noche", "la", "de", "caballero", "el", "es", "Batman"]
        palabras.reverse()

        # Para terminar unimos las palabras guardadas en el array con un espacio
        return " ".join(palabras)
        