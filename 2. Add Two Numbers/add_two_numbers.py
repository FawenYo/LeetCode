import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Simple version
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_1 = self.listnode_to_int(listnode=l1)
        num_2 = self.listnode_to_int(listnode=l2)

        result_int = num_1 + num_2

        result = self.int_to_listnode(number=result_int)
        return result

    def listnode_to_int(self, listnode: ListNode) -> int:
        """Convert List to integet

        Args:
            listnode (ListNode): input ListNode

        Returns:
            int: result integer
        """
        result = ""
        while listnode.next:
            result += f"{listnode.val}"
            listnode = listnode.next
        result += f"{listnode.val}"
        return int(result[::-1])

    def int_to_listnode(self, number: int) -> ListNode:
        """Convert integer to ListNode

        Args:
            number (int): input integer

        Returns:
            ListNode: result ListNode
        """
        result = current_node = ListNode()
        while number // 10 != 0:
            last_number = number % 10
            current_node.next = ListNode(val=last_number)
            current_node = current_node.next
            number = number // 10
        current_node.next = ListNode(val=number)
        return result.next


# Advanced version
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = current_listnode = ListNode()
        # Record for carry usage
        quotient = 0

        while l1 or l2 or quotient:
            value_l1 = value_l2 = 0
            if l1:
                value_l1 = l1.val
                l1 = l1.next
            if l2:
                value_l2 = l2.val
                l2 = l2.next

            # Update quotient and insert ListNode
            quotient, remainder = divmod(value_l1 + value_l2 + quotient, 10)
            current_listnode.next = ListNode(val=remainder)
            current_listnode = current_listnode.next
        return result.next


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
