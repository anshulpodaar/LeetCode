"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from typing import List
import copy

class Solution:
    @classmethod
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new_matrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            curr_array = matrix[i]
            for j in range(len(curr_array)):
                new_matrix[j][-i-1] = curr_array[j]
        print(f"Input: {matrix} \nOutput: {new_matrix} \n\n")
        matrix = new_matrix
        return None


def _main():
    Solution.rotate(matrix=[[1,2],[3,4]])
    Solution.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]])
    Solution.rotate(matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])


if __name__ == '__main__':
    _main()
