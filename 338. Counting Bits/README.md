# [338. Counting Bits](https://leetcode.com/problems/counting-bits/) - Medium

## Question

Given an integer `` num ``, return _an array of the number of_ `` 1 ``_'s in the binary representation of every number in the range_ `` [0, num] ``.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> num = 2
<strong>Output:</strong> [0,1,1]
<strong>Explanation:</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> num = 5
<strong>Output:</strong> [0,1,1,2,1,2]
<strong>Explanation:</strong>
0 --&gt; 0
1 --&gt; 1
2 --&gt; 10
3 --&gt; 11
4 --&gt; 100
5 --&gt; 101
</pre>

&nbsp;

__Constraints:__

* <code>0 &lt;= num &lt;= 10<sup>5</sup></code>

&nbsp;

__Follow up:__

* It is very easy to come up with a solution with run time `` O(32n) ``. Can you do it in linear time `` O(n) `` and possibly in a single pass?
* Could you solve it in `` O(n) `` space complexity?
* Can you do it without using any built-in function (i.e., like `` __builtin_popcount `` in C++)?

## Answer

本題的核心概念只需判斷是否為2的倍數，而我們可以使用移動bit `i >> 1` 的方式更快速地計算

```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num + 1):
            # >>: Bit-shifting, same as i // 2
            counter.append(counter[i >> 1] + i % 2)
        return counter

```
