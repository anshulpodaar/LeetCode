"""
https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from typing import Optional
import copy

from utils.linked_list_utils import list_to_linked_list, linked_list_to_list, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list_head = None
        while head:
            new_node = ListNode(head.val)
            temp = new_list_head
            new_list_head = new_node
            new_list_head.next = temp
            head = head.next
        return new_list_head


    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list_head = None
        while head:
            new_node = ListNode(head.val)
            temp = new_list_head
            new_list_head = new_node
            new_list_head.next = temp
            head = head.next
        return new_list_head

    # def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     new_list_head = None
    #     return new_list_head

    def reverse_list_inplace(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        prev_node = None
        curr_node = head
        next_node = head.next

        while curr_node is not None:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            if curr_node is not None:
                next_node = next_node.next
                head = curr_node

        return head


def _test():
    test_scenarios = [
        {
            "input": [1, 2, 3, 4, 5],
            "expected": [5, 4, 3, 2, 1]
        },
        {
            "input": [1, 2],
            "expected": [2, 1]
        },
        {
            "input": [],
            "expected": []
        }
    ]

    my_solution = Solution()

    for i, scenario in enumerate(test_scenarios):
        print(f"\n---------- \nTest scenario {i}")
        # input_list_head = list_to_linked_list(scenario["input"])

        # Test Iterative Solution
        print("Testing Iterative Solution")
        input_list_head = list_to_linked_list(scenario["input"])
        output_list_head = my_solution.reverseList(head=input_list_head)
        assert linked_list_to_list(output_list_head) == scenario["expected"], f"Test scenario {i} failed"
        print("Iterative Solution passed\n")

        # Test Recursive Solution
        # print("Testing Recursive Solution")
        # print("Recursive Solution passed\n")

        # Test Inplace Solution
        print("Testing Inplace Solution")
        input_list_head = list_to_linked_list(scenario["input"])
        input_list_head = my_solution.reverse_list_inplace(head=input_list_head)
        assert linked_list_to_list(input_list_head) == scenario["expected"], f"Test scenario {i} failed"
        print("Inplace Solution passed\n")

    print("\n---------- \nExecution completed!\n---------- \n")


# def test_reverse_list():
#     test_scenarios = [
#         {
#             "input": [[1, 2, 3, 4, 5]],
#             "expected": [5, 4, 3, 2, 1]
#         },
#         {
#             "input": [[1, 2]],
#             "expected": [2, 1]
#         },
#         {
#             "input": [[]],
#             "expected": []
#         }
#     ]
#
#     for i, scenario in enumerate(test_scenarios):
#         input_list = copy.deepcopy(scenario["input"])
#         output_list = Solution.reverseList(head=input_list)
#         assert output_list == scenario["expected"], f"Test scenario {i} failed"


if __name__ == '__main__':
    _test()
