# [48. Rotate Image](https://leetcode.com/problems/rotate-image/) - Medium

## Question

You are given an _n_ x _n_ 2D `` matrix `` representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">__in-place__</a>, which means you have to modify the input 2D matrix directly. __DO NOT__ allocate another 2D matrix and do the rotation.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="width: 642px; height: 242px;"/>

<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [[7,4,1],[8,5,2],[9,6,3]]
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="width: 800px; height: 321px;"/>

<pre>
<strong>Input:</strong> matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
<strong>Output:</strong> [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> matrix = [[1]]
<strong>Output:</strong> [[1]]
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> matrix = [[1,2],[3,4]]
<strong>Output:</strong> [[3,1],[4,2]]
</pre>

&nbsp;

__Constraints:__

* `` matrix.length == n ``
* `` matrix[i].length == n ``
* <code> 1 &lt;= n &lt;= 20 </code>
* <code> -1000 &lt;= matrix[i][j] &lt;= 1000 </code>

## Answer

本題要翻轉矩陣，需要具備線性代數的基本概念 (我沒有QwQ)

在這邊分享看到其他人解題的方法，只需要兩步驟即可解決：

1. 將矩陣中`row 和 column 的數值對調`
2. 將`每一個row的數值前後對調`，即可完成90度翻轉

圖像解說： ![解說影片](https://i.imgur.com/HzN4QvK.gif)

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the Matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(len(matrix)):
            row_length = len(matrix[i]) - 1
            for j in range(row_length):
                if j * 2 > row_length:
                    break
                matrix[i][j], matrix[i][row_length - j] = (
                    matrix[i][row_length - j],
                    matrix[i][j],
                )

```
