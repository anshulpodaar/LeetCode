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
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        x_str = str(x)
        while len(x_str) > 1:
            if x_str[0] == x_str[-1]:
                x_str = x_str[1:-1]
                if len(x_str) == 0:
                    return True
                x_new = int(x_str)
                Solution.isPalindrome(x_new)
            else:
                return False
        return True

    # TODO: Follow up: Could you solve it without converting the integer to a string?

def _main():
    print(Solution.isPalindrome(1234321))
    print(Solution.isPalindrome(12344321))
    print(Solution.isPalindrome(1234564321))
    print(Solution.isPalindrome(1))
    print(Solution.isPalindrome(None))


if __name__ == '__main__':
    _main()
