"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

from typing import List, Tuple


class Solution:
    @classmethod
    def search_insert(cls, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if not nums:
            return 0
        elif target <= nums[left]:
            return 0
        elif target == nums[right]:
            return right
        elif target > nums[right]:
            return right + 1

        while left <= right:
            mid_idx = left + int((right - left + 1) / 2)
            mid_val = nums[mid_idx]
            if target == mid_val:
                return mid_idx
            elif target < mid_val:
                right = mid_idx
            elif target > mid_val:
                left = mid_idx
            if right - left <= 1:
                return right


def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [1, 3, 5, 6],
            'target': 5,
            'expected': 2
        },
        {
            'nums': [1, 3, 5, 6],
            'target': 2,
            'expected': 1
        },
        {
            'nums': [1, 3, 5, 6],
            'target': 7,
            'expected': 4
        },
        {
            'nums': [1, 3, 5, 6],
            'target': 0,
            'expected': 0
        },
        {
            'nums': [1, 3, 5, 6],
            'target': -1,
            'expected': 0
        },
        {
            'nums': [1, 3],
            'target': 1,
            'expected': 0
        },
        {
            'nums': [],
            'target': 1,
            'expected': 0
        },
        {
            'nums': [1],
            'target': 1,
            'expected': 0
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().search_insert(nums=test_case['nums'], target=test_case['target'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
