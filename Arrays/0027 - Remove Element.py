# tags: Array, Two Pointer

"""
27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result be
placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the
first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
extra memory.

Custom Judge:
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List, Tuple


class Solution:
    def remove_element(self, nums: List[int], val: int) -> Tuple[int, List[int]]:
        k = 0
        len_nums = len(nums)

        left, right = 0, len_nums - 1

        while left <= right:
            if nums[left] != val:
                left += 1
                k += 1
            else:
                nums[left] = nums[right]
                right -= 1

        return k, nums


def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [3, 2, 2, 3],
            'val': 3,
            'expected_len': 2,
            'expected_nums': [2, 2, 0, 0],
        },
        {
            'nums': [0, 1, 2, 2, 3, 0, 4, 2],
            'val': 2,
            'expected_len': 5,
            'expected_nums': [0, 1, 4, 0, 3, 0, 0, 0],
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result_len, result_nums = Solution().remove_element(nums=test_case['nums'], val=test_case['val'])
        print(f'Result: {result_len = }, {result_nums = }')
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
