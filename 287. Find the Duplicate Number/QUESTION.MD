# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) - Medium

## Question

Given an array of integers `` nums `` containing&nbsp;`` n + 1 `` integers where each integer is in the range `` [1, n] `` inclusive.

There is only __one repeated number__ in `` nums ``, return _this&nbsp;repeated&nbsp;number_.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,3,4,2,2]
<strong>Output:</strong> 2
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [3,1,3,4,2]
<strong>Output:</strong> 3
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> 1
</pre>

__Example 4:__

<pre><strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

* <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
* `` nums.length == n + 1 ``
* <code> 1 &lt;= nums[i] &lt;= n </code>
* All the integers in `` nums `` appear only __once__ except for __precisely one integer__ which appears __two or more__ times.

&nbsp;

__Follow up:__

* How can we prove that at least one duplicate number must exist in `` nums ``?
* Can you solve the problem __without__ modifying the array `` nums ``?
* Can you solve the problem using only constant, `` O(1) `` extra space?
* Can you solve the problem with runtime complexity less than <code>O(n<sup>2</sup>)</code>?
