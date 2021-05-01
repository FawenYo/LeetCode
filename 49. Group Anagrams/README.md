# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) - Medium

## Question

Given an array of strings `` strs ``, group __the anagrams__ together. You can return the answer in __any order__.

An __Anagram__ is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

__Example 2:__

<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre>

__Example 3:__

<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code>
* <code> 0 &lt;= strs[i].length &lt;= 100 </code>
* `` strs[i] `` consists of lower-case English letters.

## Answer

本題關鍵點在對列表的內容進行排序，之後再返回 `map` 的 `values` 即可求得答案

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for each in strs:
            key = tuple(sorted(each))
            if key in map:
                map[key].append(each)
            else:
                map[key] = [each]
        return list(map.values())

```
