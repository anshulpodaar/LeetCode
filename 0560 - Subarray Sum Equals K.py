"""
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

from typing import Optional, List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums.sort()
        n = 0
        i = 0
        prefix_sum_array = []
        while i < len(nums):
            if i == 0:
                prefix_sum_array.append(nums[i])
            else:
                prefix_sum_array.append(prefix_sum_array[i-1] + nums[i])
            i += 1

        left, right = -1, 0
        while left < len(prefix_sum_array) and right < len(prefix_sum_array):
            if left == -1:
                if prefix_sum_array[right] == k:
                    n += 1
                    right += 1
                elif prefix_sum_array[right] < k:
                    right += 1
                else:
                    left += 1
            else:
                if prefix_sum_array[right] - prefix_sum_array[left] == k:
                    n += 1
                    right += 1
                elif prefix_sum_array[right] - prefix_sum_array[left] < k:
                    right += 1
                else:
                    left += 1

        return n

        # while left < len(prefix_sum_array) and right < len(prefix_sum_array):
        #     if left == -1:
        #         if prefix_sum_array[right] == k:
        #             n += 1
        #             left += 1
        #             right += 1
        #         elif prefix_sum_array[right] < k:
        #             right += 1
        #         else:
        #             left += 1
        #     else:
        #         if prefix_sum_array[right] - prefix_sum_array[left] == k:
        #             n += 1
        #             left += 1
        #             right += 1
        #         elif prefix_sum_array[right] - prefix_sum_array[left] < k:
        #             right += 1
        #         else:
        #             left += 1
        # return n


def _test():
    test_scenarios = [
        # {
        #     "input": [1, 1, 1],
        #     "k": 2,
        #     "expected": 2,
        # },
        # {
        #     "input": [1, 2, 3],
        #     "k": 3,
        #     "expected": 2,
        # },
        # {
        #     "input": [1, 3, 2],
        #     "k": 3,
        #     "expected": 1,
        # },
        {
            "input": [-3, -2, -1, 0, 1, 2, 3],
            "k": 0,
            "expected": 4,
        },
    ]

    my_solution = Solution()

    flag = True
    for i, scenario in enumerate(test_scenarios):
        nums = scenario["input"]
        k = scenario["k"]
        output = my_solution.subarraySum(nums=nums, k=k)
        print(f"\n---------- \nTest scenario {i}: "
              f"\n\tinput: {scenario['input']} "
              f"\n\tk: {scenario['k']}"
              f"\n\texpected: {scenario['expected']}"
              f"\n\toutput: {output}")
        try:
            assert output == scenario["expected"]
            print("\tResult: PASSED")
        except AssertionError as e:
            flag = False
            print("\tResult: FAILED")
            print(e)

    print("\n----------")
    if flag:
        print("All test scenarios passed!")
    else:
        print("Some test scenarios failed!")
    print("Execution completed!")
    print("----------")


if __name__ == '__main__':
    _test()
