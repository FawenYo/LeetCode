# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Medium

## Question

Given the `head` of a linked list, remove the $n^{th}$ node from the end of the list and return its head.

**Follow up**: Could you do this in one pass?

## Examples

### Example 1:

![Example image](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```shell
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:

```shell
Input: head = [1], n = 1
Output: []
```

### Example 3:

```shell
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints:

* The number of nodes in the list is `sz`.
* $1 \leq sz \leq 30$
* $0 \leq Node.val \leq 100$
* $1 \leq n \leq sz$

## Answer

分別建立 `before` 和 `after` 兩個ListNode，`after`先跑n步，當`after`跑到底的時候，`before.next`就是要移除的Node。

```python
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

```
