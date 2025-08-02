"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit
of the integer. The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""
from typing import List


class Solution:
    @classmethod
    def plus_one(self, digits: List[int]) -> List[int]:

        n = len(digits)

        while n >= 0:
            if n == 0:
                digits.insert(0, 1)
                return digits
            if digits[n - 1] != 9:
                digits[n - 1] += 1
                return digits
            elif digits[n - 1] == 9:
                digits[n - 1] = 0
                n -= 1
        return None


def _main():
    Solution()
    my_test_cases = [
        {
            'digits': [1, 2, 3],
            'expected': [1, 2, 4]
        },
        {
            'digits': [4, 3, 2, 1],
            'expected': [4, 3, 2, 2]
        },
        {
            'digits': [9],
            'expected': [1, 0]
        },
        {
            'digits': [6, 9],
            'expected': [7, 0]
        },
        {
            'digits': [],
            'expected': [1]
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().plus_one(digits=test_case['digits'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
