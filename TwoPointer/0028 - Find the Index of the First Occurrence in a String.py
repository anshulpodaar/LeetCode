"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    @classmethod
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_needle==0 or len_haystack==0:
            return -1
        if needle in haystack:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i + len_needle] == needle:
                    return i
        return -1


def _main():
    Solution()
    my_test_cases = [
        {
            'haystack': 'sadbutsad',
            'needle': 'sad',
            'expected': 0
        },
        {
            'haystack': 'leetcode',
            'needle': 'leeto',
            'expected': -1
        },
        {
            'haystack': '',
            'needle': 'leeto',
            'expected': -1
        },
        {
            'haystack': '',
            'needle': '',
            'expected': -1
        },
        {
            'haystack': 'aaabbbccc',
            'needle': 'bbb',
            'expected': 3
        },
        {
            'haystack': 'bbb',
            'needle': 'aaabbbccc',
            'expected': -1
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().strStr(haystack=test_case['haystack'], needle=test_case['needle'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
