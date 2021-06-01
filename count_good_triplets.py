class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    	triplet_count = 0
    	for i in range(len(arr)):
    		for j in range(j+1, len(arr)):
    			for k in range(j+1, len(arr)):
    				a_round = abs(arr[i] - arr[j]) <= a
    				b_round = abs(arr[j] - arr[k]) <= b
    				c_round = abs(arr[i] - arr[k]) <= c

    				if a_round and b_round and c_round:
    					triplet_count += 1
    	return triplet_count
        

# loop through for arr[i] <= a
# loop through for arr[j] <= b
# loop through for arr[k] <= c

# check if arr[i] -  arr[j]
# check if arr[j] - arr[k]
# check if arr[k] -  len(arr)

# if all three pass, then increase the triplet count






# 1534. Count Good Triplets
# Easy


# Given an array of integers (arr), and three integers (a, b and c).
# You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good
# if the following conditions are true:

# •	0 <= i < j < k < arr.length
# •	|arr[i] - arr[j]| <= a
# •	|arr[j] - arr[k]| <= b
# •	|arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.
 
# Example 1:
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

# Example 2:
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.


