# tags: HashMap, String

"""
205 - Isomorphic Strings.
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
    The strings s and t can be made identical by:
    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
    The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true


Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    @classmethod
    def is_isomorphic_strings(cls, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_substitution_map = {}

        for i in range(len(s)):
            if s[i] not in letter_substitution_map.keys():
                if t[i] not in letter_substitution_map.values():
                    letter_substitution_map[s[i]] = t[i]
                elif s[i] != t[i]:
                    letter_substitution_map[s[i]] = s[i]
                else:
                    return False

            if letter_substitution_map[s[i]] != t[i]:
                return False
        return True



def _main():
    Solution()
    my_test_cases = [
        {
            's': 'egg',
            't': 'add',
            'expected': True
        },
        {
            's': 'foo',
            't': 'bar',
            'expected': False
        },
        {
            's': 'paper',
            't': 'title',
            'expected': True
        },
        {
            's': 'badc',
            't': 'baba',
            'expected': False
        },
        {
            's': 'bab',
            't': 'baba',
            'expected': False
        },
        {
            's': 'egcd',
            't': 'adfd',
            'expected': False
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().is_isomorphic_strings(s=test_case['s'], t=test_case['t'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
