import sys

sys.path.append(".")
from model import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        after = before = head
        # After = start from nth
        for _ in range(n):
            after = after.next
        if not after:
            return head.next
        # Got last nth when after ended
        while after.next:
            after = after.next
            before = before.next

        before.next = before.next.next
        return head


if __name__ == "__main__":
    head = list_to_listnode(target=[1, 2, 3, 4, 5])
    n = 2
    answer = Solution().removeNthFromEnd(head=head, n=n)
    print(listnode_to_list(answer))
