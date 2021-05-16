# [198. House Robber](https://leetcode.com/problems/house-robber/) - Medium

## Question

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and __it will automatically contact the police if two adjacent houses were broken into on the same night__.

Given an integer array `` nums `` representing the amount of money of each house, return _the maximum amount of money you can rob tonight __without alerting the police___.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= nums.length &lt;= 100 </code>
* <code> 0 &lt;= nums[i] &lt;= 400 </code>
