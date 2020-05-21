'''
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
'''
==========================================================================================================
class Solution(object):                                                                                  
    def countSquares(self, matrix):                                                                      
        n = len(matrix)                                                                                  
        m = len(matrix[0])
        ans = [[0] * (m + 1) for i in range(n + 1)]
        count = 0
        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if(matrix[row - 1][col - 1] == 1):
                    ans[row][col] = 1 + min(ans[row][col - 1], ans[row - 1][col], ans[row - 1][col - 1])
                    count += ans[row][col]
        return count
==========================================================================================================
