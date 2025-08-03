"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


class Solution:
    @classmethod
    def climb_stairs(cls, n: int) -> int:
        if n <= 3 and n >= 0: return n

        prev1 = 3
        prev2 = 2
        cur = 0

        for _ in range(3, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur

        return cur


def _main():
    Solution()
    my_test_cases = [
        {
            'n': 1,
            'expected': 1
        },
        {
            'n': 2,
            'expected': 2
        },
        {
            'n': 3,
            'expected': 3
        },
        {
            'n': 4,
            'expected': 5
        },
        {
            'n': 5,
            'expected': 8
        },
        {
            'n': 6,
            'expected': 13
        },
        {
            'n': 7,
            'expected': 21
        },
        {
            'n': 8,
            'expected': 34
        },
        {
            'n': 9,
            'expected': 55
        },
        {
            'n': 10,
            'expected': 89
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().climb_stairs(n=test_case['n'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
