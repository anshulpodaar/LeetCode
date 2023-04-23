"""
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

import typing
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def print_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        prev = head
        curr = head.next
        temp = head.next.next
        while temp:
            curr.next = prev
            prev = curr
            curr = temp
            temp = temp.next
        curr.next = prev
        head.next = None
        head = curr
        return head

    # def reverseList_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None:
    #         return None
    #     elif head.next is None:
    #         return head
    #     prev = head
    #     curr = head.next
    #     temp = head.next.next
    #     if temp:
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
    #         temp = temp.next
    #         self.reverseList_recursion(head)
    #     curr.next = prev
    #     head.next = None
    #     head = curr
    #     return head


def _main():
    test = Solution()
    ll1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ll2 = ListNode(1, ListNode(2))
    ll3 = None
    ll4 = ListNode(1)

    test.print_list(ll1)
    ll1 = test.reverseList(ll1)
    test.print_list(ll1)

    print()

    test.print_list(ll2)
    ll2 = test.reverseList(ll2)
    test.print_list(ll2)

    print()

    test.print_list(ll3)
    ll3 = test.reverseList(ll3)
    test.print_list(ll3)

    print()

    test.print_list(ll4)
    ll3 = test.reverseList(ll4)
    test.print_list(ll4)


# def _main_recursion():
#     test = Solution()
#     ll1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#     ll2 = ListNode(1, ListNode(2))
#     ll3 = None
#     ll4 = ListNode(1)
#
#     test.print_list(ll1)
#     ll1 = test.reverseList_recursion(ll1)
#     test.print_list(ll1)
#
#     print()
#
#     test.print_list(ll2)
#     ll2 = test.reverseList_recursion(ll2)
#     test.print_list(ll2)
#
#     print()
#
#     test.print_list(ll3)
#     ll3 = test.reverseList_recursion(ll3)
#     test.print_list(ll3)
#
#     print()
#
#     test.print_list(ll4)
#     ll3 = test.reverseList_recursion(ll4)
#     test.print_list(ll4)


if __name__ == "__main__":
    _main()
    # _main_recursion()
