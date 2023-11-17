class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        word = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
        def base_convert(i, b):
            result = []
            while i > 0:
                i -= 1
                result.insert(0, i % b)
                i = i // b
            return result
        res = base_convert(columnNumber, 26)
        resul = ''
        for i in res:
            resul += word[i]
        return resul