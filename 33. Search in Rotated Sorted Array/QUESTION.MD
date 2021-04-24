# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Medium

## Question

There is an integer array `` nums `` sorted in ascending order (with __distinct__ values).

Prior to being passed to your function, <code> nums `` is __rotated__ at an unknown pivot index `` k `` (`` 0 &lt;= k &lt; nums.length ``) such that the resulting array is `` [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] `` (__0-indexed__). For example, `` [0,1,2,4,5,6,7] `` might be rotated at pivot index `` 3 `` and become `` [4,5,6,7,0,1,2] </code>.

Given the array `` nums `` __after__ the rotation and an integer `` target ``, return _the index of _`` target ``_ if it is in _`` nums ``_, or _`` -1 ``_ if it is not in _`` nums ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= nums.length &lt;= 5000 </code>
* <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>
* All values of `` nums `` are __unique__.
* `` nums `` is guaranteed to be rotated at some pivot.
* <code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code>

&nbsp;
__Follow up:__ Can you achieve this in `` O(log n) `` time complexity?
