class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])

        dummy_matrix=[[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                dummy_matrix[j][row-1-i]=matrix[i][j]
        
        for i in range(row):
            for j in range(col):
                matrix[i][j]=dummy_matrix[i][j]
        
