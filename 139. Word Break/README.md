# [139. Word Break](https://leetcode.com/problems/word-break/) - Medium

## Question

Given a string `` s `` and a dictionary of strings `` wordDict ``, return `` true `` if `` s `` can be segmented into a space-separated sequence of one or more dictionary words.

__Note__ that the same word in the dictionary may be reused multiple times in the segmentation.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "leetcode", wordDict = ["leet","code"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "leetcode" can be segmented as "leet code".
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "applepenapple", wordDict = ["apple","pen"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= s.length &lt;= 300 </code>
* <code> 1 &lt;= wordDict.length &lt;= 1000 </code>
* <code> 1 &lt;= wordDict[i].length &lt;= 20 </code>
* `` s `` and `` wordDict[i] `` consist of only lowercase English letters.
* All the strings of `` wordDict `` are __unique__.

## Answer

利用 DP 演算法解題。可以參考 [YouTube 教學影片](https://www.youtube.com/watch?v=tSbBuiO1rXI)

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # ex. ["", "l", "le", "lee", "leet", "leetc", "leetco", "leetcod", "leetcode"]
        dp = [True] + [False] * len(s)

        for index in range(1, len(s) + 1):

            for word in wordDict:
                if dp[index - len(word)] and s[:index].endswith(word):
                    dp[index] = True

        return dp[-1]

```
