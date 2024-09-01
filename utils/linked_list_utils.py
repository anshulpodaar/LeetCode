from typing import List, Optional

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(input_list: List[int]) -> Optional[ListNode]:
    """
    Convert a list of integers into a linked list.
    Args:
        input_list: List[int]: List of integers to be converted into a linked list.
    Returns:
        ListNode: The head of the linked list.
    """
    if len(input_list) == 0:
        return None
    head = ListNode(input_list[0])
    current_node = head
    for i in range(1, len(input_list)):
        current_node.next = ListNode(input_list[i])
        current_node = current_node.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert a linked list into a list of integers.
    Args:
        head: ListNode: The head of the linked list.

    Returns:
        List[int]: List of integers.
    """
    current_node = head
    output_list = []
    while current_node:
        output_list.append(current_node.val)
        current_node = current_node.next
    return output_list
