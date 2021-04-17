# [136. Single Number](https://leetcode.com/problems/single-number/) - Easy

## Question

Given a __non-empty__&nbsp;array of integers `` nums ``, every element appears _twice_ except for one. Find that single one.

__Follow up:__&nbsp;Could you implement a solution with a linear runtime complexity and without using extra memory?

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [2,2,1]
<strong>Output:</strong> 1
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
* <code>-3 * 10<sup>4</sup> &lt;= nums[i] &lt;= 3 * 10<sup>4</sup></code>
* Each element in the array appears twice except for one element which appears only once.

## Answer

這邊提供3種做法

### 作法1: 直觀

這應該是最簡單最直觀的方法，只要紀錄曾經出現過的內容就可以找到只出現過1次的答案。

### 作法2: 加總

本題限制中提到每個內容最多只會重複2次，且只有一個答案，因此只要把 `nums加總` - `set加總 * 2`

### 作法3: XOR

可以透過XOR運算找到沒有重複的值

```python
# Simple method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        result = []
        for number in nums:
            if number not in seen:
                result.append(number)
            elif number in result:
                result.remove(number)
            seen[number] = 1
        return result[0]


# Sum method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        distinct_sum = sum(set(nums))
        return distinct_sum * 2 - sum(nums)


# XOR method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """XOR calculate

        | a   | b   | a ^ b |
        | --- | --- | ----- |
        | 0   | 0   | 0     |
        | 0   | 1   | 1     |
        | 1   | 0   | 1     |
        | 1   | 1   | 0     |

        a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        """
        result = 0
        for number in nums:
            result ^= number
        return result

```
