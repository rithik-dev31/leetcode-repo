# Last updated: 8/12/2026, 11:32:28 AM
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows,cols=len(matrix),len(matrix[0])

        row_zero=False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0

                    if r>0:
                        matrix[r][0]=0
                    else:
                        row_zero=True

        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for i in range(rows):
                matrix[i][0]=0

        if row_zero:
            for j in range(cols):
                matrix[0][j]=0