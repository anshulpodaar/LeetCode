# tags: Array, Math, Two Pointers

"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List, Union


class Solution:
    def __init__(self):
        pass

    @classmethod
    def rotate(cls, nums: List[int], k: int) -> Union[None, List[int]]:
        """
        Do not return anything, modify nums in-place instead.
        - For my local tests, I will return the array nums to avoid writing a different unit test.
        """
        # Array solution
        len_nums = len(nums)
        if len_nums <= 1 or k % len_nums == 0:
            return nums  # No rotation needed

        k %= len_nums
        nums[:] = nums[-k:] + nums[:-k]
        return nums


    def rotate_2(self, nums: List[int], k: int) -> Union[None, List[int]]:
        # Pointer solution
        len_nums = len(nums)
        if len_nums <= 1 or k % len_nums == 0:
            return nums

        while k > 0:
            nums = self.shift_one(nums)
            k -= 1

        return nums


    def shift_one(self, nums: List[int]) -> Union[None, List[int]]:
        len_nums = len(nums)
        temp = nums[len_nums - 1]
        count = len_nums-1
        while count > 0:
            nums[count] = nums[count-1]
            count -= 1
        nums[0] = temp
        return nums








def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [1,2,3,4,5,6,7],
            'k': 3,
            'expected': [5,6,7,1,2,3,4]
        },
        {
            'nums': [-1,-100,3,99],
            'k': 2,
            'expected': [3,99,-1,-100]
        },
        {
            'nums': [],
            'k': 2,
            'expected': []
        },
        {
            'nums': [1,2],
            'k': 7,
            'expected': [2,1]
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().rotate_2(nums=test_case['nums'], k=test_case['k'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
