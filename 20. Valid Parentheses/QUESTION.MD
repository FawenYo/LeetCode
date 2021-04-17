# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Easy

## Question

Given a string `` s `` containing just the characters `` '(' ``, `` ')' ``, `` '{' ``, `` '}' ``, `` '[' `` and `` ']' ``, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "([)]"
<strong>Output:</strong> false
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "{[]}"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
* `` s `` consists of parentheses only `` '()[]{}' ``.
