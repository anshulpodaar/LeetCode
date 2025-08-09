# tags: HashMap, String, Counting
"""
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
from typing import Dict


class Solution:
    @classmethod
    def can_construct(cls, ransom_note: str, magazine: str) -> bool:
        if not all(letter in magazine for letter in ransom_note):
            return False

        ransom_count = cls.letters_in_string_counter(ransom_note)
        magazine_count = cls.letters_in_string_counter(magazine)
        return all(magazine_count[c] >= ransom_count[c] for c in ransom_count)

    @classmethod
    def letters_in_string_counter(cls, string: str) -> Dict[str, int]:
        count_map = {}
        for letter in string:
            if letter not in count_map:
                count_map[letter] = 1
            else:
                count_map[letter] += 1
        return count_map


def _main():
    Solution()
    my_test_cases = [
        {
            'ransom_note': 'a',
            'magazine': 'b',
            'expected': False
        },
        {
            'ransom_note': 'aa',
            'magazine': 'ab',
            'expected': False
        },
        {
            'ransom_note': 'aa',
            'magazine': 'aab',
            'expected': True
        },
        {
            'ransom_note': 'hello',
            'magazine': 'hello to you too',
            'expected': False
        },
        {
            'ransom_note': 'hello',
            'magazine': 'yello to you too',
            'expected': False
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().can_construct(ransom_note=test_case['ransom_note'], magazine=test_case['magazine'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
