"""
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List, Union


class Solution:
    @classmethod
    def majority_element(cls, nums: List[int]) -> Union[int, None]:
        if not nums:
            return None

        nums.sort()

        return nums[len(nums) // 2]

    @classmethod
    def majority_element_2(cls, nums: List[int]) -> Union[int, None]:
        nums_count = {}
        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1

        for num in nums_count:
            if nums_count[num] > len(nums) // 2:
                return num
        return None


def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [3, 2, 3],
            'expected': 3
        },
        {
            'nums': [2, 2, 1, 1, 1, 2, 2],
            'expected': 2
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().majority_element(nums=test_case['nums'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
