# tags: HashTable, String, Sorting

"""
0242.

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    @classmethod
    def is_anagram(cls, s: str, t: str) -> bool:
        letter_count = {}
        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1
        for letter in t:
            letter_count[letter] = letter_count.get(letter, 0) - 1
        if any(letter_count.values()) != 0:
            return False
        else:
            return True



def _main():
    Solution()
    my_test_cases = [
        {
            's': 'anagram',
            't': 'nagaram',
            'expected': True
        },
        {
            's': 'rat',
            't': 'car',
            'expected': False
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().is_anagram(s=test_case['s'], t=test_case['t'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()

