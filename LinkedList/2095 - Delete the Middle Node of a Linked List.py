"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.

Constraints:
The number of nodes in the list is in the range [1, 10**5].
1 <= Node.val <= 10**5
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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            head = None
            return head
        new_node = ListNode()
        new_node.next = head
        slow = fast = head
        prev = new_node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next
        prev.next = slow.next
        return head


def _main():
    test = Solution()
    ll1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ll2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    ll3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    ll4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    ll5 = ListNode(1)

    test.print_list(ll1)
    test.deleteMiddle(ll1)
    test.print_list(ll1)
    print()
    test.print_list(ll2)
    test.deleteMiddle(ll2)
    test.print_list(ll2)
    print()
    test.print_list(ll3)
    test.deleteMiddle(ll3)
    test.print_list(ll3)
    print()
    test.print_list(ll4)
    test.deleteMiddle(ll4)
    test.print_list(ll4)
    print()
    test.print_list(ll5)
    test.deleteMiddle(ll5)
    test.print_list(ll5)


if __name__ == "__main__":
    _main()
