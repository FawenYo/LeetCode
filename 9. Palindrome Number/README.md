# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) - Easy

## Question

Given an integer `` x ``, return `` true `` if `` x `` is palindrome integer.

An integer is a __palindrome__ when it reads the same backward as forward. For example, `` 121 `` is palindrome while `` 123 `` is not.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> x = -101
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

* <code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code>

&nbsp;
__Follow up:__ Could you solve it without converting the integer to a string?

## Answer

With string: 反轉 $x$ 並比對是否相同

Without string: 透過餘數抓最後一個數值，反轉後比對是否相同

```python
# With string version
class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_data = str(x)
        return input_data[::-1] == input_data


# Without string version
class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = x
        reverse = 0
        if x < 0:
            return False
        else:
            while x > 0:
                last_number = x % 10
                reverse = reverse * 10 + last_number
                x = x // 10
            if origin == reverse:
                return True
            else:
                return False

```
