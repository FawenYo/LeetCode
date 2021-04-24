# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Easy

## Question

You are climbing a staircase. It takes `` n `` steps to reach the top.

Each time you can either climb `` 1 `` or `` 2 `` steps. In how many distinct ways can you climb to the top?

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= n &lt;= 45 </code>

## Answer

從 `n=3` 的情況我們可以觀察到，最後一步可以走 `1` 或 `2` 階樓梯，分別對應到 `n=2` 和 `n=1` 的解，因此我們可以得出 `n(i) = n(i - 1) + n(i - 2)` 的結論

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            result = 0
            previous = 1
            current = 2
            for _ in range(n - 2):
                result = previous + current
                previous = current
                current = result
            return result

```
