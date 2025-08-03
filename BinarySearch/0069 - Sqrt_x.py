"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 2^31 - 1
"""


class Solution:
    @classmethod
    def my_sqrt(cls, x: int) -> int:

        # if x == 0 or x == 1:
        #     return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1

        return right


def _main():
    Solution()
    my_test_cases = [
        {
            'input': 0,
            'expected': 0
        },
        {
            'input': 1,
            'expected': 1
        },
        {
            'input': 2,
            'expected': 1
        },
        {
            'input': 3,
            'expected': 1
        },
        {
            'input': 4,
            'expected': 2
        },
        {
            'input': 5,
            'expected': 2
        },
        {
            'input': 6,
            'expected': 2
        },
        {
            'input': 7,
            'expected': 2
        },
        {
            'input': 8,
            'expected': 2
        },
        {
            'input': 9,
            'expected': 3
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().my_sqrt(x=test_case['input'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
