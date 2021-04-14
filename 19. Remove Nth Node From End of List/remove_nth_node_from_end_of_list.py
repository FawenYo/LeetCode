from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    # Convert List to ListNode
    def list_to_listnode(target: List[int]) -> ListNode:
        result = current_node = ListNode()
        for each in target:
            current_node.next = ListNode(val=each)
            current_node = current_node.next
        return result.next

    # Convert ListNode to List
    def listnode_to_list(listnode: ListNode) -> List[int]:
        result = []
        while listnode.next:
            result.append(listnode.val)
            listnode = listnode.next
        result.append(listnode.val)
        return result

    head = list_to_listnode(target=[1, 2, 3, 4, 5])
    n = 2
    answer = Solution().removeNthFromEnd(head=head, n=n)
    print(listnode_to_list(answer))