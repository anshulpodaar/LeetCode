# tags: HashMap, String

"""
0290 - Word Pattern
https://leetcode.com/problems/word-pattern/description/

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.


Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
    The bijection can be established as:
        'a' maps to "dog".
        'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    @classmethod
    def word_pattern2(cls, pattern: str, s: str) -> bool:
        words = list(s.strip().split())
        if len(words) != len(pattern):
            return False

        word_sub_map = {}
        for i in range(len(pattern)):
            if pattern[i] in word_sub_map.keys():
                if word_sub_map[pattern[i]] != words[i]:
                    return False
                else:
                    continue
            elif pattern[i] not in word_sub_map.keys():
                if words[i] not in word_sub_map.values():
                    word_sub_map[pattern[i]] = words[i]
                    continue
                elif words[i] in word_sub_map.values():
                    return False
        return True


    def word_pattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split()
        if len(pattern) != len(words):
            return False

        hm = {}
        used = set()

        for ch, word in zip(pattern, words):
            if ch in hm:
                if hm[ch] != word:
                    return False
            else:
                if word in used:
                    return False
                hm[ch] = word
                used.add(word)
        return True



def _main():
    Solution()
    my_test_cases = [
        {
            'pattern': 'abba',
            's': 'dog cat cat dog',
            'expected': True
        },
        {
            'pattern': 'abba',
            's': 'dog cat cat fish',
            'expected': False
        },
        {
            'pattern': 'aaaa',
            's': 'dog cat cat dog',
            'expected': False
        },

        {
            'pattern': 'abb',
            's': 'dog cat cat dog',
            'expected': False
        },
        {
            'pattern': 'abba',
            's': 'dog cat cat ',
            'expected': False
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().word_pattern(pattern=test_case['pattern'], s=test_case['s'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
