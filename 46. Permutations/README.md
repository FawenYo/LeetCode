# [46. Permutations](https://leetcode.com/problems/permutations/) - Medium

## Question

Given an array `` nums `` of distinct integers, return _all the possible permutations_. You can return the answer in __any order__.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> [[0,1],[1,0]]
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [[1]]
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= nums.length &lt;= 6 </code>
* <code> -10 &lt;= nums[i] &lt;= 10 </code>
* All the integers of `` nums `` are __unique__.

## Answer

使用DFS演算法解題，走到底時其路徑便是答案。

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = self.dfs(nums=nums, path=[], result=[])
        return result

    def dfs(self, nums, path, result):
        # Deepest
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            # Except for current num
            new_nums = nums[:i] + nums[i + 1 :]
            # Add current num to path
            new_path = path + [nums[i]]
            self.dfs(nums=new_nums, path=new_path, result=result)
        return result
  
```
