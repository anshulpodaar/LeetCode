# tags: Array, Dynamic Programming

"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List

from jedi.inference.gradual.typing import Tuple


class Solution:
    @classmethod
    def max_profit(cls, prices: List[int]) -> int:

        # max_profit = 0
        # buy_idx, sell_idx = None, None
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if max_profit < prices[j] - prices[i]:
        #             max_profit = prices[j] - prices[i]
        #             buy_idx, sell_idx = i, j
        # return max_profit

        # if not prices:
        #     return 0
        if len(prices) < 2:
            return 0

        profit = 0
        buy = prices[0]
        sell = None
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif profit < prices[i] - buy:
                profit = prices[i] - buy

        return profit


def _main():
    Solution()
    my_test_cases = [
        {
            'prices': [7, 1, 5, 3, 6, 4],
            'expected': 5
        },
        {
            'prices': [7, 6, 4, 3, 1],
            'expected': 0
        },
    ]

    for i, test_case in enumerate(my_test_cases):
        print('\n--------------------------\n')
        print(f'Test case {i}: {test_case}')
        result = Solution().max_profit(prices=test_case['prices'])
        print(f'Result: {result}')
        try:
            assert result == test_case['expected']
            print(f'Test case {i}: Pass')
        except AssertionError:
            print(f'Error: Expected {test_case["expected"]}, but got {result}')


if __name__ == '__main__':
    _main()
