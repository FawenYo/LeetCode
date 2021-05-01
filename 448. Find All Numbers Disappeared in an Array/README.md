# [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) - Easy

## Question

Given an array `` nums `` of `` n `` integers where `` nums[i] `` is in the range `` [1, n] ``, return _an array of all the integers in the range_ `` [1, n] `` _that do not appear in_ `` nums ``.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [4,3,2,7,8,2,3,1]
<strong>Output:</strong> [5,6]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [2]
</pre>

&nbsp;

__Constraints:__

* `` n == nums.length ``
* <code>1 &lt;= n &lt;= 10<sup>5</sup></code>
* <code> 1 &lt;= nums[i] &lt;= n </code>

&nbsp;

__Follow up:__ Could you do it without extra space and in `` O(n) `` runtime? You may assume the returned list does not count as extra space.

## Answer

本題如果直接檢查 `in nums` 的話很容易會 Time Limit Exceeded，關鍵點是利用 `set` 的方式排除重複的內容，增加檢查效率

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        num_set = set(nums)
        for number in range(1, len(nums) + 1):
            if number not in num_set:
                result.append(number)
        return result

```
