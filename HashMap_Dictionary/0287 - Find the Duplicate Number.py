"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        for num, count in num_counts.items():
            if count > 1:
                return num
        return None


def _main():
    my_solution = Solution()
    print(my_solution.findDuplicate(nums=[1,3,4,2,2]))
    print(my_solution.findDuplicate(nums=[3,1,3,4,2]))


if __name__ == '__main__':
    _main()
