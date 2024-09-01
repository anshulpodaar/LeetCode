"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying
the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]


Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

from typing import Optional

from utils.linked_list_utils import list_to_linked_list, linked_list_to_list, ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev_node = ListNode()
        prev_node.next = head
        head = prev_node
        curr_node = head.next
        next_node = curr_node.next

        while curr_node is not None and next_node is not None:
            prev_node.next = next_node
            curr_node.next = next_node.next
            next_node.next = curr_node

            prev_node = curr_node
            curr_node = curr_node.next
            next_node = curr_node.next if curr_node is not None else None

        head = head.next
        return head


def _test():
    test_scenarios = [
        {
            "input": [1, 2, 3, 4],
            "expected": [2, 1, 4, 3],
        },
        {
            "input": [],
            "expected": [],
        },
        {
            "input": [1],
            "expected": [1],
        },
        {
            "input": [1, 2, 3, 4, 5],
            "expected": [2, 1, 4, 3, 5],
        },
        {
            "input": [1, 2, 3, 4, 5, 6],
            "expected": [2, 1, 4, 3, 6, 5],
        },
    ]

    my_solution = Solution()

    flag = True
    for i, scenario in enumerate(test_scenarios):
        input_list_head = list_to_linked_list(scenario["input"])
        output_list_head = my_solution.swapPairs(head=input_list_head)
        output_list = linked_list_to_list(output_list_head)
        print(f"\n---------- \nTest scenario {i}: "
              f"\n\tinput: {scenario['input']} "
              f"\n\texpected: {scenario['expected']}"
              f"\n\toutput: {output_list}")
        try:
            assert output_list == scenario["expected"]
            print("\tResult: PASSED")
        except AssertionError as e:
            flag = False
            print("\tResult: FAILED")
            print(e)

    print("\n----------")
    if flag:
        print("All test scenarios passed!")
    else:
        print("Some test scenarios failed!")
    print("Execution completed!")
    print("----------")


if __name__ == '__main__':
    _test()
