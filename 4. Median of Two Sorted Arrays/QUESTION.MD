# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) - Hard

## Question

Given two sorted arrays `` nums1 `` and `` nums2 `` of size `` m `` and `` n `` respectively, return __the median__ of the two sorted arrays.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums1 = [1,3], nums2 = [2]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> merged array = [1,2,3] and median is 2.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [3,4]
<strong>Output:</strong> 2.50000
<strong>Explanation:</strong> merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums1 = [0,0], nums2 = [0,0]
<strong>Output:</strong> 0.00000
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> nums1 = [], nums2 = [1]
<strong>Output:</strong> 1.00000
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> nums1 = [2], nums2 = []
<strong>Output:</strong> 2.00000
</pre>

&nbsp;

__Constraints:__

* `` nums1.length == m ``
* `` nums2.length == n ``
* <code> 0 &lt;= m &lt;= 1000 </code>
* <code> 0 &lt;= n &lt;= 1000 </code>
* <code> 1 &lt;= m + n &lt;= 2000 </code>
* <code>-10<sup>6</sup> &lt;= nums1[i], nums2[i] &lt;= 10<sup>6</sup></code>

&nbsp;
__Follow up:__ The overall run time complexity should be `` O(log (m+n)) ``.
