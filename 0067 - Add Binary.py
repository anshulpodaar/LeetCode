"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
from typing import Tuple, Union


class Solution:
    @classmethod
    def add_binary(cls, a: str, b: str) -> str:
        carry = 0
        res = []

        idx_a, idx_b = len(a) - 1, len(b) - 1

        while idx_a >= 0 or idx_b >= 0 or carry == 1:
            if idx_a >= 0:
                carry += int(a[idx_a])
                idx_a -= 1
            if idx_b >= 0:
                carry += int(b[idx_b])
                idx_b -= 1

            res.append(str(carry % 2))   # remainder of division
            carry = carry // 2   # floor of division

        return "".join(res[::-1])


    @classmethod
    def add_binary_2(cls, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    @classmethod
    def add_binary_0(cls, a: str, b: str) -> str:

        idx_a = len(a) - 1
        idx_b = len(b) - 1
        result = ''
        carry: bool = 0

        while idx_a >= 0 or idx_b >= 0 or carry:
            res_str = ''

            if idx_a >= 0:
                sub_str_a = a[idx_a]
                idx_a -= 1
            else:
                sub_str_a = ''

            if idx_b >= 0:
                sub_str_b = b[idx_b]
                idx_b -= 1
            else:
                sub_str_b = ''

            res_str, carry = cls.add_one_digit(
                                            sub_str_a=sub_str_a,
                                            sub_str_b=sub_str_b,
                                            carry=carry,
                                        )
            result = res_str + result

        return result

    @classmethod
    def add_one_digit(
            cls,
            sub_str_a: str,  # Union['0', '1', ''],
            sub_str_b: str,  # Union['0', '1', ''],
            carry: bool,  # Union['1', '']
    ) -> Tuple[str, bool]:
        sub_str_res = ''
        if (sub_str_a == '0' or sub_str_a == '') and (sub_str_b == '0' or sub_str_b == ''):
            if carry:
                sub_str_res = '1'
                carry = 0
            elif not carry:
                sub_str_res = '0'
                # carry = 0

        elif sub_str_a == '1' and sub_str_b == '1':
            if carry:
                sub_str_res = '1'
                carry = 1
            elif not carry:
                sub_str_res = '0'
                carry = 1

        elif sub_str_a == '1' or sub_str_b == '1':
            if carry:
                sub_str_res = '0'
                carry = 1
            elif not carry:
                sub_str_res = '1'
                carry = 0

        elif not (sub_str_a) and not (sub_str_b) and carry:
            sub_str_res = '1'
            carry = 0

        return sub_str_res, carry




def _main():
    Solution()
    my_test_cases = [
        {
            'a': '11',
            'b': '1',
            'expected': '100'
        },
        {
            'a': '1010',
            'b': '1011',
            'expected': '10101'
        },
        {
            'a': '1111',
            'b': '1111',
            'expected': '11110'
        },
        {
            'a': '11',
            'b': '1',
            'expected': '100'
        },
        {
            'a': '1',
            'b': '11',
            'expected': '100'
        },
        {
            'a': '1',
            'b': '',
            'expected': '1'
        },
        {
            'a': '',
            'b': '1',
            'expected': '1'
        },
        {
            'a': '',
            'b': '',
            'expected': ''
        },
        {
            'a': '100',
            'b': '110010',
            'expected': '110110'
        },
        {
            'a': '111',
            'b': '11',
            'expected': '1010'
        },
        {
            'a': '11',
            'b': '11',
            'expected': '110'
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().add_binary(a=test_case['a'], b=test_case['b'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
