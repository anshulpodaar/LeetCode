"""
https://leetcode.com/problems/reverse-linked-list-ii/description/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

from typing import Optional

from utils.linked_list_utils import list_to_linked_list, linked_list_to_list, ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Initialize the left and right nodes
        left_node = head
        left_prev = ListNode(None)
        left_prev.next = left_node
        i = 0
        while i < left - 1:
            left_prev = left_node
            left_node = left_node.next
            i += 1
        right_node = left_node
        while i < right - 1:
            right_node = right_node.next
            i += 1
        right_next = right_node.next
        right_node.next = None

        # Reverse the nodes between left and right
        new_reversed_head, new_reversed_tail = self.reverse_list_inplace(head=left_node)
        left_prev.next = new_reversed_head
        new_reversed_tail.next = right_next
        if left == 1:
            head = new_reversed_head
        # Return the head of the linked list
        return head

    def reverse_list_inplace(self, head: Optional[ListNode]) -> [Optional[ListNode], Optional[ListNode]]:

        if head is None:
            return None, None

        prev_node = None
        curr_node = head
        next_node = head.next
        tail = curr_node

        while curr_node is not None:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            if curr_node is not None:
                next_node = next_node.next
                head = curr_node

        return head, tail


def _test():
    test_scenarios = [
        {
            "input": [1, 2, 3, 4, 5],
            "left": 2,
            "right": 4,
            "expected": [1, 4, 3, 2, 5],
        },
        {
            "input": [5],
            "left": 1,
            "right": 1,
            "expected": [5],
        },
        {
            "input": [1, 2, 3, 4, 5, 6],
            "left": 2,
            "right": 4,
            "expected": [1, 4, 3, 2, 5, 6],
        },
        {
            "input": [3, 5],
            "left": 1,
            "right": 2,
            "expected": [5, 3],
        },
        {
            "input": [1, 2, 3, 4, 5],
            "left": 1,
            "right": 5,
            "expected": [5, 4, 3, 2, 1],
        },
    ]

    my_solution = Solution()

    for i, scenario in enumerate(test_scenarios):
        input_list_head = list_to_linked_list(scenario["input"])
        left = scenario["left"]
        right = scenario["right"]
        output_list_head = my_solution.reverseBetween(head=input_list_head, left=left, right=right)
        try:
            assert linked_list_to_list(output_list_head) == scenario["expected"]
            print(f"Test scenario {i}: passed")
        except AssertionError as e:
            print(f"Test scenario {i}: failed")
            print(e)

    print("\n---------- \nExecution completed!\n---------- \n")


if __name__ == '__main__':
    _test()
