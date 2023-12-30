class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #FIRST SOLUTION
        def char_to_int(char):
            return ord(char) - ord('0')

        first_number = 0
        for char in num1:
            first_number = first_number * 10 + char_to_int(char)

        second_number = 0
        for char in num2:
            second_number = second_number * 10 + char_to_int(char)

        return str(first_number * second_number)
        #SECOND SOLUTION
        digits = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        first_number = 0
        second_number = 0
        for i in range(len(num1)):
            first_number = (first_number * 10) + digits[num1[i]]
        for j in range(len(num2)):
            second_number = (second_number * 10) + digits[num2[j]]
        return str(first_number * second_number)
