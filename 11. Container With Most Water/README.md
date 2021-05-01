# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) - Medium

## Question

Given `` n `` non-negative integers <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code><sub> </sub>, where each represents a point at coordinate <code>(i, a<sub>i</sub>)</code>. `` n `` vertical lines are drawn such that the two endpoints of the line `` i `` is at <code>(i, a<sub>i</sub>)</code> and `` (i, 0) ``. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

__Notice__ that you may not slant the container.

&nbsp;

__Example 1:__

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;"/>

<pre>
<strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> height = [4,3,2,1,4]
<strong>Output:</strong> 16
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> height = [1,2,1]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

* `` n == height.length ``
* <code>2 &lt;= n &lt;= 10<sup>5</sup></code>
* <code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code>

## Answer

本題的關鍵點在固定住較高的點，並逐漸將另外一點內縮，直到兩點交會時便能求得答案

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        first_point = 0
        last_point = len(height) - 1
        while first_point != last_point:
            if height[first_point] > height[last_point]:
                temp = height[last_point] * (last_point - first_point)
                if temp > result:
                    result = temp
                # Move last point inward
                last_point -= 1
            else:
                temp = height[first_point] * (last_point - first_point)
                if temp > result:
                    result = temp
                # Move first point inward
                first_point += 1
        return result

```
