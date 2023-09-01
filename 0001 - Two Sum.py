"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        value = None
        for index_num, num in enumerate(nums):
            residual = target - num
            # nums[index_num] = None
            if residual in nums and nums.index(residual) != index_num:
                index_residual = nums.index(residual)
                value = list((index_num, index_residual))
                break
        print(value)
        return value

    @classmethod
    def twoSum_2(cls, nums: list[int], target: int) -> list[list[int]]:
        value = []
        for index_num, num in enumerate(nums):
            if num == target:
                value.append([index_num])
                continue
            residual = target - num
            nums[index_num] = None
            if residual in nums:
                index_residual = nums.index(residual)
                value.append(list((index_num, index_residual)))
        print(value)
        return value

    @classmethod
    def twoSum_3(cls, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]


def _main():
    Solution.twoSum(nums=[1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum(nums=[0, 1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum(nums=[3, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum(nums=[3, 3], target=6)
    Solution.twoSum_2(nums=[1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum_2(nums=[0, 1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum_3(nums=[1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum_3(nums=[0, 1, 2, 3, 4, 5, 6, 7], target=6)


if __name__ == '__main__':
    _main()
