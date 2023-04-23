"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional
import typing


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def pop_first(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head
        head = head.next
        temp.next = None
        return temp, head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None and list2:
            return list2
        elif list2 is None and list1:
            return list1

        head = None
        tail = None
        while list1 or list2:
            if list1 is None and list2:
                temp, list2 = self.pop_first(list2)
            elif list2 is None and list1:
                temp, list1 = self.pop_first(list1)
            elif list1 and list2:
                if list1.val <= list2.val:
                    temp, list1 = self.pop_first(list1)
                else:
                    temp, list2 = self.pop_first(list2)
            if head is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = temp
        return head


def _main():
    test = Solution()

    print(f"---------- Iteration 1 ----------")
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    test.print_list(list1)
    print()
    test.print_list(list2)
    print()
    merged_list = test.mergeTwoLists(list1, list2)
    test.print_list(merged_list)

    print()
    print(f"---------- Iteration 2 ----------")
    list1 = None
    list2 = None
    test.print_list(list1)
    print()
    test.print_list(list2)
    print()
    merged_list = test.mergeTwoLists(list1, list2)
    test.print_list(merged_list)


    print()
    print(f"---------- Iteration 3 ----------")
    list1 = None
    list2 = ListNode(0)
    test.print_list(list1)
    print()
    test.print_list(list2)
    print()
    merged_list = test.mergeTwoLists(list1, list2)
    test.print_list(merged_list)

    print()
    print(f"---------- Iteration 4 ----------")
    list1 = ListNode(2, ListNode(5, ListNode(6)))
    list2 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
    test.print_list(list1)
    print()
    test.print_list(list2)
    print()
    merged_list = test.mergeTwoLists(list1, list2)
    test.print_list(merged_list)

    print()
    print(f"---------- Iteration 4 ----------")
    list1 = ListNode(-10, ListNode(-9, ListNode(-6, ListNode(-4, ListNode(1, ListNode(9, ListNode(9)))))))
    list2 = ListNode(-5, ListNode(-3, ListNode(0, ListNode(7, ListNode(8, ListNode(8))))))
    test.print_list(list1)
    print()
    test.print_list(list2)
    print()
    merged_list = test.mergeTwoLists(list1, list2)
    test.print_list(merged_list)


if __name__ == "__main__":
    _main()

# TODO: not fixed yet
