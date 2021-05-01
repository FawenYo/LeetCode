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
