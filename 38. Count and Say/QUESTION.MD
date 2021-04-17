# [38. Count and Say](https://leetcode.com/problems/count-and-say/) - Medium

## Question

The __count-and-say__ sequence is a sequence of digit strings defined by the recursive formula:

* `` countAndSay(1) = "1" ``
* `` countAndSay(n) `` is the way you would "say" the digit string from `` countAndSay(n-1) ``, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the __minimal__ number of groups so that each group is a contiguous section all of the __same character.__ Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string `` "3322251" ``:

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg" style="width: 581px; height: 172px;"/>

Given a positive integer `` n ``, return _the _<code>n<sup>th</sup></code>_ term of the __count-and-say__ sequence_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> "1"
<strong>Explanation:</strong> This is the base case.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> "1211"
<strong>Explanation:</strong>
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= n &lt;= 30 </code>
