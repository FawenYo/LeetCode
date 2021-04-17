# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Medium

## Question

Given a string `` s ``, find the length of the __longest substring__ without repeating characters.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abcabcbb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "abc", with the length of 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "bbbbb"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is "b", with the length of 1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "pwwkew"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

* <code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code>
* `` s `` consists of English letters, digits, symbols and spaces.
