# tags: Array, Dynamic Programming, Greedy

"""
55. Jump Game

You are given an integer array nums.
You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    @classmethod
    def can_jump(cls, nums: List[int]) -> bool:
        if not nums:
            return False

        max_reach = nums[0]
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True





def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [2,3,1,1,4],
            'expected': True
        },
        {
            'nums': [3,2,1,0,4],
            'expected': False
        },
        {
            'nums': [],
            'expected': False
        },
        {
            'nums': [5],
            'expected': True
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().can_jump(nums=test_case['nums'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
