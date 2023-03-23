"""
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore, it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

from math import floor, log10


class Solution:
    @staticmethod
    def isPalindrome(x: int or None) -> bool:
        # TODO: inefficient
        x_str = str(x)
        while len(x_str) > 1:
            if x_str[0] == x_str[-1]:
                x_str = x_str[1:-1]
                if len(x_str) == 0:
                    return True
                # # TODO: unnecessary
                # x_new = int(x_str)
                # # TODO: not needed recursion
                # Solution.isPalindrome(x_new)
            else:
                return False
        return True

    # TODO: Follow up: Could you solve it without converting the integer to a string?
    @staticmethod
    def isPalindrome_2(x: int) -> int:
        num = x
        if x:
            no_of_digits = floor(log10(abs(x))) + 1
        else:
            return False
        power = no_of_digits - 1
        y = 0
        while x != 0:
            y = y + ((x%10) * 10**power)
            x = int(x/10)
            power = power - 1
        if y == num:
            return True
        else:
            return False


def _main():
    print(Solution.isPalindrome(1234321))
    print(Solution.isPalindrome(-1234321))
    print(Solution.isPalindrome(12344321))
    print(Solution.isPalindrome(12345654321))
    print(Solution.isPalindrome(1))
    print(Solution.isPalindrome(None))

    print()
    # print(reverseInt(1))
    # print(reverseInt(12))
    # print(reverseInt(123))
    # print(reverseInt(1234))
    # print(reverseInt(12345))
    # print(reverseInt(-12345))
    print()

    print(Solution.isPalindrome_2(1234321))
    print(Solution.isPalindrome_2(-1234321))
    print(Solution.isPalindrome_2(12344321))
    print(Solution.isPalindrome_2(12345654321))
    print(Solution.isPalindrome_2(1))
    print(Solution.isPalindrome_2(None))


if __name__ == '__main__':
    _main()
