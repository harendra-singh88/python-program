class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
        num = 0
        prev_value = 0

        for char in reversed(s):  # Start from the end of the string
            value = roman_map[char]
            if value < prev_value:
                num =num-value
            else:
                num =num+value
            prev_value = value

        print(num)

# Example
new1 = Solution()
new1.romanToInt("DXLII")  # Output should be 
