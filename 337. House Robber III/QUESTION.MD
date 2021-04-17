# [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) - Medium

## Question

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `` root ``.

Besides the `` root ``, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if __two directly-linked houses were broken into on the same night__.

Given the `` root `` of the binary tree, return _the maximum amount of money the thief can rob __without alerting the police___.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg" style="width: 277px; height: 293px;"/>

<pre>
<strong>Input:</strong> root = [3,2,3,null,3,null,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg" style="width: 357px; height: 293px;"/>

<pre>
<strong>Input:</strong> root = [3,4,5,1,3,null,1]
<strong>Output:</strong> 9
<strong>Explanation:</strong> Maximum amount of money the thief can rob = 4 + 5 = 9.
</pre>

&nbsp;

__Constraints:__

* The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.
* <code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code>
