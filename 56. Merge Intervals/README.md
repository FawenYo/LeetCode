# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Medium

## Question

Given an array&nbsp;of `` intervals ``&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code>
* `` intervals[i].length == 2 ``
* <code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code>

## Answer

先對 `internals` 做排序，再去檢查每一個 `start` 是否比前一個 `end` 小，如果是的話再重新算 `end` 就好


```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        else:
            result = []

            intervals.sort()
            temp_start, temp_end = intervals[0]
            for start, end in intervals[1:]:
                if start <= temp_end:
                    temp_end = max(temp_end, end)
                else:
                    result.append([temp_start, temp_end])
                    temp_start = start
                    temp_end = end
            result.append([temp_start, temp_end])
            return result

```
