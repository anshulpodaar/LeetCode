"""
https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    @staticmethod
    def romanToInt(roman: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0

        for i in range(len(roman)):
            if i+1 < len(roman) and roman_map[roman[i]] < roman_map[roman[i+1]]:
                integer -= roman_map[roman[i]]
            else:
                integer += roman_map[roman[i]]

        print(f'Roman: {roman} --> Integer: {integer}')
        return integer


def _main():
    print("\nWIP - this is not my solution, but copied from discussions\n")
    # TODO: Solve on my own

    Solution.romanToInt('IV')
    Solution.romanToInt('IX')
    Solution.romanToInt('VIII')
    Solution.romanToInt('XXIV')
    Solution.romanToInt('XLII')
    Solution.romanToInt('XL')
    Solution.romanToInt('XLV')
    Solution.romanToInt('MMCDLXXIX')


if __name__ == '__main__':
    _main()
