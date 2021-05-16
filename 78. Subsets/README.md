# [78. Subsets](https://leetcode.com/problems/subsets/) - Medium

## Question

Given an integer array `` nums `` of __unique__ elements, return _all possible subsets (the power set)_.

The solution set __must not__ contain duplicate subsets. Return the solution in __any order__.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= nums.length &lt;= 10 </code>
* <code> -10 &lt;= nums[i] &lt;= 10 </code>
* All the numbers of&nbsp;`` nums `` are __unique__.

## Answer

排列組合

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

```
