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
        print(f"Input: {matrix}")
        matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(int(len(matrix)/2)):
                temp = copy.deepcopy(matrix[i][j])
                matrix[i][j] = copy.deepcopy(matrix[i][-j-1])
                matrix[i][-j-1] = copy.deepcopy(temp)
                # matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        print(f"Output: {matrix} \n\n")
        return None


    @classmethod
    def transpose(self, matrix: List[List[int]]) -> None:
        print(f"Input: {matrix}")
        matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(int(len(matrix) / 2)):
                temp = copy.deepcopy(matrix[i][j])
                matrix[i][j] = copy.deepcopy(matrix[i][-j - 1])
                matrix[i][-j - 1] = copy.deepcopy(temp)
                # matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        print(f"Output: {matrix} \n\n")
        return None


def _main():
    # Solution.rotate(matrix=[[1,2],[3,4]])
    # Solution.rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]])
    # Solution.rotate(matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
    Solution.transpose(matrix=[[11, 12, 13, 14],
                            [21, 22, 23, 24],
                            [31, 32, 33, 34],
                            [41, 42, 43, 44]])


if __name__ == '__main__':
    _main()
