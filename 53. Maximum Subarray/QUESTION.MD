# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Easy

## Question

Given an integer array `` nums ``, find the contiguous subarray (containing at least one number) which has the largest sum and return _its sum_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [4,-1,2,1] has the largest sum = 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
* <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>

&nbsp;
__Follow up:__ If you have figured out the `` O(n) `` solution, try coding another solution using the __divide and conquer__ approach, which is more subtle.
