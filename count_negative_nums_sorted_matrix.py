# faster than 80%
# less memory than 75%

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
    	count = 0
    	for row in grid:
    		for num in row:
    			if num < 0:
    				count += 1
    	return count
        




#steps
# iterate through each array
# count everything that is less than 0


# 1351. Count Negative Numbers in a Sorted Matrix
# Easy

# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

# Example 1:

# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:

# Input: grid = [[1,-1],[-1,-1]]
# Output: 3