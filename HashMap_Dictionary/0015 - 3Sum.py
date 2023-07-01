"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
- 3 <= nums.length <= 3000
- -10**5 <= nums[i] <= 10**5
"""

from typing import List
from itertools import combinations


class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        value = None
        nums_copy = nums.copy()
        for index_num, num in enumerate(nums_copy):
            residual = target - num
            nums_copy[index_num] = None
            if residual in nums_copy:
                index_residual = nums_copy.index(residual)
                value = list((index_num, index_residual))
                break
        # print(value)
        return value

    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        sol = []
        for num in nums:
            nums_copy = nums.copy()
            residual = 0 - num
            nums_copy.remove(num)
            two_sum = Solution.twoSum(nums_copy, residual)
            if two_sum is not None:
                sol.append([num, nums[two_sum[0]], nums[two_sum[1]]])
        return sol


    @staticmethod
    def threeSum2(nums: List[int]) -> List[List[int]]:
        sol = []
        combs = combinations(nums, 3)
        for comb in combs:
            if sum(comb) == 0:
                if sorted(list(comb)) not in sol:
                    sol.append(sorted(list(comb)))
        return sol



def _main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution.threeSum(nums))
    # nums = [0, 1, 1]
    # print(Solution.threeSum(nums))
    # nums = [0, 0, 0]
    # print(Solution.threeSum(nums))


if __name__ == "__main__":
    _main()



