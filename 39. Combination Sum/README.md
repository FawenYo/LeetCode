# [39. Combination Sum](https://leetcode.com/problems/combination-sum/) - Medium

## Question

Given an array of __distinct__ integers `` candidates `` and a target integer `` target ``, return _a list of all __unique combinations__ of _`` candidates ``_ where the chosen numbers sum to _`` target ``_._ You may return the combinations in __any order__.

The __same__ number may be chosen from `` candidates `` an __unlimited number of times__. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is __guaranteed__ that the number of unique combinations that sum up to `` target `` is less than `` 150 `` combinations for the given input.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> candidates = [2,3,6,7], target = 7
<strong>Output:</strong> [[2,2,3],[7]]
<strong>Explanation:</strong>
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> candidates = [2,3,5], target = 8
<strong>Output:</strong> [[2,2,2,2],[2,3,3],[3,5]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> candidates = [2], target = 1
<strong>Output:</strong> []
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> candidates = [1], target = 1
<strong>Output:</strong> [[1]]
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> candidates = [1], target = 2
<strong>Output:</strong> [[1,1]]
</pre>

&nbsp;

__Constraints:__

* <code> 1 &lt;= candidates.length &lt;= 30 </code>
* <code> 1 &lt;= candidates[i] &lt;= 200 </code>
* All elements of `` candidates `` are __distinct__.
* <code> 1 &lt;= target &lt;= 500 </code>

## Answer

本題使用 DFS 方式解題，sort 用意為在發現 target < 0 後能直接break


```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = self.dfs(candidates=candidates, path=[], result=[], target=target)
        return result

    def dfs(
        self,
        candidates: List[int],
        path: List[int],
        result: List[List[int]],
        target: int,
    ):
        if target < 0:
            return None
        if target == 0:
            result.append(path)

        for i in range(len(candidates)):
            new_candidates = candidates[i:]
            new_path = path + [candidates[i]]
            new_target = target - candidates[i]
            # No more result
            if new_target < 0:
                break
            self.dfs(
                candidates=new_candidates,
                path=new_path,
                result=result,
                target=new_target,
            )
        return result

```
