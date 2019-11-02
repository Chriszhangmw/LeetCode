'''

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

'''
import  numpy as np
def uniquePaths(m,n):
    path = np.zeros([m,n])
    for i in range(m):
        for j in range(n):
            if i ==0 or j ==0:
                path[i][j] = 1
            else:
                path[i][j] = path[i-1][j] + path[i][j-1]
    return path[m-1][n-1]





