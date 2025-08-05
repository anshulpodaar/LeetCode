"""
80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that
each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

from typing import List, Tuple

# TODO: Improve Complexity, currently slow

class Solution:
    def removeDuplicates(self, nums: List[int]) -> Tuple[int, List[int]]:

        nums_len = len(nums)

        if nums_len < 2:
            k = nums_len
            return k, nums

        k, i = 1, 1
        max_val = nums[0]
        count = 1
        while i < nums_len:
            if count < 2:
                if nums[i] == max_val:
                    count += 1
                else:
                    count = 1
                nums[k] = nums[i]
                max_val = nums[k]
                i += 1
                k += 1
            else:
                if nums[i] <= max_val:
                    i += 1
                else:
                    while i < nums_len and nums[i] == nums[k - 1]:
                        i += 1
                    nums[k] = nums[i]
                    max_val = nums[k]
                    i += 1
                    k += 1
                    count = 1

        return k, nums


def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [1, 1, 1, 2, 2, 3],
            'expected_nums': [1, 1, 2, 2, 3, 0],
            'expected_len': 5,
        },
        {
            'nums': [1, 2, 2, 2, 2, 3],
            'expected_nums': [1, 2, 2, 3, 0, 0],
            'expected_len': 4,
        },
        {
            'nums': [0, 0, 1, 1, 1, 1, 2, 3, 3],
            'expected_nums': [0, 0, 1, 1, 2, 3, 3, 0, 0],
            'expected_len': 7,
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result_len, result_nums = Solution().removeDuplicates(nums=test_case['nums'])
        print(f'Result: {result_nums = }, {result_len = }')
        try:
            assert result_len == test_case['expected_len']
            for n in range(result_len):
                assert result_nums[n] == test_case['expected_nums'][n]
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected_len"] = }, but got {result_len}')
            print(f'Error: Expected {test_case["expected_nums"] = }, but got {result_nums}')


if __name__ == '__main__':
    _main()
