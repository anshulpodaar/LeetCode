"""

"""



class Solution:
    @classmethod
    def my_func(cls):
        pass


def _main():
    Solution()
    my_test_cases = [
        {
            'nums': [1, 3, 5, 6],
            'target': 5,
            'expected': 2
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().my_func(nums=test_case['nums'], target=test_case['target'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
