"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1.
The 0 is only there to ensure the merge result can fit in nums1.


Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""
from typing import List, Union


class Solution:
    @classmethod
    def merge(cls, nums1: List[int], m: int, nums2: List[int], n: int) -> Union[None, List[int]]:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0
        while i < m + n and j < n:
            if (nums1[i] > nums2[j]) or (m == 0) or (i >= m + j):
                k = m + j
                while k > i:
                    nums1[k] = nums1[k-1]
                    k -= 1
                nums1[i] = nums2[j]
                j += 1
            i += 1
        return nums1 # Returning for my testcase validation only


def _main():
    Solution()
    my_test_cases = [
        {
            'nums1': [1, 2, 3, 0, 0, 0],
            'm': 3,
            'nums2': [2, 5, 6],
            'n': 3,
            'expected': [1,2,2,3,5,6]
        },
        {
            'nums1': [1],
            'm': 1,
            'nums2': [],
            'n': 0,
            'expected': [1]
        },
        {
            'nums1': [0],
            'm': 0,
            'nums2': [1],
            'n': 1,
            'expected': [1]
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().merge(
                                    nums1=test_case['nums1'],
                                    m=test_case['m'],
                                    nums2=test_case['nums2'],
                                    n=test_case['n']
                                    )
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
