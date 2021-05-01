# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) - Medium

## Question

You are given two __non-empty__ linked lists representing two non-negative integers. The digits are stored in __reverse order__, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;"/>

<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

&nbsp;

__Constraints:__

* The number of nodes in each linked list is in the range `` [1, 100] ``.
* <code> 0 &lt;= Node.val &lt;= 9 </code>
* It is guaranteed that the list represents a number that does not have leading zeros.

## Answer

### Simple version

先將 ListNode 轉為數字，將數字相加後反轉回 ListNode

### Advanced version

直接從 ListNode取值進行相加，並記錄除以10的商作為進位用途

```python
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

```
