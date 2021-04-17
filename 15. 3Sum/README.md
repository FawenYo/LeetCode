# [15. 3Sum](https://leetcode.com/problems/3sum/) - Medium

## Question

Given an integer array nums, return all the triplets `` [nums[i], nums[j], nums[k]] `` such that `` i != j ``, `` i != k ``, and `` j != k ``, and `` nums[i] + nums[j] + nums[k] == 0 ``.

Notice that the solution set must not contain duplicate triplets.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> []
</pre>

&nbsp;

__Constraints:__

* <code> 0 &lt;= nums.length &lt;= 3000 </code>
* <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>

## Answer

關鍵：**Dict查找速度會比List快上許多**，因為Dict是**直接尋找**值，而List則是類似**遍歷尋找**。

本題解題思路基本上和1. Two Sum 解法相近，找到兩個數字後只需檢查 `-num1-num2` 是否存在於 `nums` 內，便可解題。

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        # Sort list first
        nums.sort()

        for first_index, first_num in enumerate(nums):
            # Bypass if first_num is same with previous num
            if first_index >= 1 and first_num == nums[first_index - 1]:
                continue
            # Key point: find in dictionary has far BETTER performance than list
            remain = {}
            for second_num in nums[first_index + 1 :]:
                if second_num in remain:
                    # Found answer
                    result.add(
                        tuple(sorted((first_num, second_num, -first_num - second_num)))
                    )
                else:
                    remain[-first_num - second_num] = 1
        return sorted(result)

```
