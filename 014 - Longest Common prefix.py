"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        i=0
        min_word_length = min([len(item) for item in strs])
        flag = True
        while flag and i < min_word_length:
            letter = strs[0][i]
            if all(item[i] == letter for item in strs):
                lcp = lcp + letter
                i += 1
            else:
                flag = False
        return lcp


def _main():
    print(Solution.longestCommonPrefix(Solution(), strs = ["flower","flow","flight"]))
    print(Solution.longestCommonPrefix(Solution(), strs = ["dog","racecar","car"]))
    print(Solution.longestCommonPrefix(Solution(), strs = ["dog","doggo","doggie"]))

if __name__ == "__main__":
    _main()
