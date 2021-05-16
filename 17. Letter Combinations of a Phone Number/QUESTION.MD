# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) - Medium

## Question

Given a string containing digits from `` 2-9 `` inclusive, return all possible letter combinations that the number could represent. Return the answer in __any order__.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" style="width: 200px; height: 162px;"/>

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> digits = "23"
<strong>Output:</strong> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> digits = ""
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> digits = "2"
<strong>Output:</strong> ["a","b","c"]
</pre>

&nbsp;

__Constraints:__

* <code> 0 &lt;= digits.length &lt;= 4 </code>
* `` digits[i] `` is a digit in the range `` ['2', '9'] ``.
