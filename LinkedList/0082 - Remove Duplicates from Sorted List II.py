"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

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
        if head is None or head.next is None:
            return head
        d = {}
        curr = head
        while curr is not None:
            if curr.val in d:
                d[curr.val] += 1
            else:
                d[curr.val] = 1
            curr = curr.next
        curr = head
        new_node = ListNode()
        prev = new_node
        while curr is not None:
            if curr.next is None and d[curr.val] > 1:
                prev.next = None
            if d[curr.val] > 1:
                curr = curr.next
            else:
                prev.next = curr
                prev = prev.next
                curr = curr.next
        head = new_node.next
        return head


def _main():
    test = Solution()

    print(f"---------- Iteration 1 ----------")
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    test.print_list(list1)
    print()
    list1 = test.deleteDuplicates(list1)
    test.print_list(list1)

    print()
    print(f"---------- Iteration 2 ----------")
    list2 = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))))
    test.print_list(list2)
    print()
    list2 = test.deleteDuplicates(list2)
    test.print_list(list2)

    print(f"---------- Iteration 3 ----------")
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(5, ListNode(5)))))))))
    test.print_list(list1)
    print()
    list1 = test.deleteDuplicates(list1)
    test.print_list(list1)


if __name__ == "__main__":
    _main()