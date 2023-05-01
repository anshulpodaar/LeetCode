"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            temp = curr
            while temp:
                if temp.next and temp.next.val == curr.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            curr = curr.next
        return head


def _main():
    test = Solution()

    print(f"---------- Iteration 1 ----------")
    list1 = ListNode(1, ListNode(1, ListNode(2)))
    test.print_list(list1)
    print()
    list1 = test.deleteDuplicates(list1)
    test.print_list(list1)

    print()
    print(f"---------- Iteration 2 ----------")
    list2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    test.print_list(list2)
    print()
    list2 = test.deleteDuplicates(list2)
    test.print_list(list2)

    print(f"---------- Iteration 3 ----------")
    list3 = ListNode(1, ListNode(1, ListNode(1, ListNode(2))))
    test.print_list(list3)
    print()
    list3 = test.deleteDuplicates(list3)
    test.print_list(list3)


if __name__ == "__main__":
    _main()