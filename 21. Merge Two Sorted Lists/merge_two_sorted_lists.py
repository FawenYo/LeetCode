import sys

sys.path.append(".")
from model import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = current_node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        current_node.next = l1 or l2
        return result.next


if __name__ == "__main__":
    input_l1 = [1, 2, 4]
    input_l2 = [1, 3, 4]

    l1 = list_to_listnode(target=input_l1)
    l2 = list_to_listnode(target=input_l2)

    answer = Solution().mergeTwoLists(l1=l1, l2=l2)
    print(listnode_to_list(listnode=answer))
