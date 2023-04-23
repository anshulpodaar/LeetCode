"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
Note: Position is different than index. Position starts at 1, and both, left and right are inclusive.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
* The number of nodes in the list is n.
* 1 <= n <= 500
* -500 <= Node.val <= 500
* 1 <= left <= right <= n
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

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        prev = head
        for i in range(1, left):
            prev = prev.next
        curr = prev.next
        for i in range(1, right-left+1):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            # self.tail = curr
        head = dummy.next
        return head


def _main():
    test = Solution()
    ll1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ll2 = ListNode(5)

    test.print_list(ll1)
    ll1 = test.reverseBetween(ll1, 2, 4)
    test.print_list(ll1)

    print()

    test.print_list(ll2)
    ll2 = test.reverseBetween(ll2, 1, 1)
    test.print_list(ll2)


if __name__ == "__main__":
    _main()
