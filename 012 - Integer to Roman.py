"""
https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    @staticmethod
    def intToRoman(v: int) -> str:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        result_str = str(result)

        if v < 1 or v > 3999:
            pass
        for i in range(len(v)):
            if i == '4':
                pass

        print(f'Integer: {result} --> Roman: {s}')
        return result


    @staticmethod
    def romanToInt(roman: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0

        for i in range(len(roman)):
            if i + 1 < len(roman) and roman_map[roman[i]] < roman_map[roman[i + 1]]:
                integer -= roman_map[roman[i]]
            else:
                integer += roman_map[roman[i]]

        print(f'Roman: {roman} --> Integer: {integer}')
        return integer


def _main():
    print("\nWIP - this is not my solution, but copied from discussions\n")
    # TODO: Solve on my own

    Solution.intToRoman(4) # Roman: IV --> Integer: 4
    Solution.intToRoman(9) # Roman: IX --> Integer: 9
    Solution.intToRoman(8) # Roman: VIII --> Integer: 8
    Solution.intToRoman(24) # Roman: XXIV --> Integer: 24
    Solution.intToRoman(42) # Roman: XLII --> Integer: 42
    Solution.intToRoman(40) # Roman: XL --> Integer: 40
    Solution.intToRoman(45) # Roman: XLV --> Integer: 45
    Solution.intToRoman(2479) # Roman: MMCDLXXIX --> Integer: 2479


if __name__ == '__main__':
    _main()
