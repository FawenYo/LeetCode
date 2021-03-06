# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/) - Easy

## Question

Given a signed 32-bit integer `` x ``, return `` x ``_ with its digits reversed_. If reversing `` x `` causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return `` 0 ``.

__Assume the environment does not allow you to store 64-bit integers (signed or unsigned).__

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

__Example 2:__

<pre><strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

__Example 3:__

<pre><strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

__Example 4:__

<pre><strong>Input:</strong> x = 0
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

* <code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code>

## Answer

將 $x$ 轉為 string 後反轉

```python
class Solution:
    def reverse(self, x: int) -> int:
        input_data = str(x)
        if "-" not in input_data:
            # Directly reverse
            result = input_data[::-1]
        else:
            # Find number part
            number_part = input_data[1:]
            # -reverse_number
            result = f"-{number_part[::-1]}"
        result = int(result)
        if -(2 ** 31) < result < 2 ** 31 - 1:
            return result
        else:
            return 0

```
