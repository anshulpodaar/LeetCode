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

import typing, typing.Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val:int = 0, next: Optional[int] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1
        list2
        final_list
        return final_list_listnode




def _main():
    test = Solution()
    print(test.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))
    print(test.mergeTwoLists(list1 = [], list2 = []))
    print(test.mergeTwoLists(list1 = [], list2 = [0]))
    print(test.mergeTwoLists(list1=[2,5,6], list2=[1,3,5,7]))


if __name__ == "__main__":
    _main()

# list1 = [1, 2, 4]
# list2 = [1, 3, 4]
# print([*list1, *list2])

# TODO: not fixed yet
