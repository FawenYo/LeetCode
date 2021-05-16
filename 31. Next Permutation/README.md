# [31. Next Permutation](https://leetcode.com/problems/next-permutation/) - Medium

## Question

Implement __next permutation__, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be __<a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>__ and use only constant&nbsp;extra memory.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [1,2,3]
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1,1,5]
<strong>Output:</strong> [1,5,1]
</pre>

__Example 4:__

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= nums.length &lt;= 100 </code>
* <code> 0 &lt;= nums[i] &lt;= 100 </code>

## Answer

比較前後大小

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # Descending order
        if i == 0:
            nums.reverse()
            return None
        # Find the last "ascending" position
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        # Reverse the second part
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

```
