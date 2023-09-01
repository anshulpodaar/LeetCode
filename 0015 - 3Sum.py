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
import time


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        triplets = []
        for i in range(len(nums)):
            target = -(nums[i])
            d = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in d:
                    triplets.append(sorted([nums[i], target - nums[j], nums[j]]))
                else:
                    d[nums[j]] = j

        return sorted(list(set(map(tuple, triplets))))


    @staticmethod
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[i] + nums[j] + nums[k]) < 0:
                    j = j + 1
                    while nums[j] == nums[j - 1] and j < k:
                        j = j + 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                    while nums[k] == nums[k + 1] and j < k:
                        k = k - 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    while nums[j] == nums[j - 1] and j < k:
                        j = j + 1
                    while nums[k] == nums[k + 1] and j < k:
                        k = k - 1
        return triplets


    @staticmethod
    def threeSum4(nums: List[int]) -> List[List[int]]:
        sol = []
        num_map = {}
        for i, num in enumerate(nums):
            residual = 0 - num
            # two_sum = Solution.twoSum(nums[i + 1:], residual)
            nums_copy = nums.copy()
            nums_copy.remove(num)
            two_sum = Solution.twoSum(nums_copy, residual)
            if len(two_sum) > 0:
                num_map[num] = [[num, item[0], item[1]] for item in two_sum]
        for items in num_map.values():
            for item in items:
                if sorted(item) not in sol:
                    sol.append(sorted(item))
        return sol

    @staticmethod
    def twoSum4(nums: List[int], target: int) -> List[List[int]]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums and nums.index(complement) != i:
                num_map[num] = complement
        sol = []
        for key, val in num_map.items():
            if sorted([key, val]) not in sol:
                sol.append(sorted([key, val]))
        return sol


    @staticmethod
    def twoSum3(nums: list[int], target: int) -> list[int]:
        value = []
        for index_num, num in enumerate(nums):
            residual = target - num
            if residual in nums and nums.index(residual) != index_num:
                value.append([num, residual])
        return value


    @staticmethod
    def threeSum3(nums: List[int]) -> List[List[int]]:
        sol = []
        for num in nums:
            nums_copy = nums.copy()
            residual = 0 - num
            nums_copy.remove(num)
            two_sum = Solution.twoSum3(nums_copy, residual)
            if len(two_sum) > 0:
                for combination in two_sum:
                    val_to_append = [num, combination[0], combination[1]]
                    if sorted(list(val_to_append)) not in sol:
                        sol.append(sorted(list(val_to_append)))
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
    nums = [0, 1, 1]
    print(Solution.threeSum(nums))
    nums = [0, 0, 0]
    print(Solution.threeSum(nums))
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(Solution.threeSum(nums))


def _troubleshoot():
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    # print(Solution.twoSum(nums, 0))

    start_time = time.time()
    print(Solution.threeSum(nums))
    end_time = time.time()
    print("Execution Time: {:.3f} ms".format((end_time - start_time)*1000))

    start_time = time.time()
    print(Solution.threeSum3(nums))
    end_time = time.time()
    print("Execution Time: {:.3f} ms".format((end_time - start_time)*1000))


if __name__ == "__main__":
    # _main()
    _troubleshoot()
