class Solution:
	def findLucky(self, arr: List[int]) -> int:
		cache = {}
		for num in sorted(arr, reverse=True):
			if num not in cache.keys():
				cache[num] = 1
			else:
				cache[num] += 1
		for k, v in cache.items():
			if k == v:
				return k
		return -1

# def findLucky(arr):
#     cache = {}
#     for num in sorted(arr, reverse=True):
#     	if num not in cache.keys():
#     		cache[num] = 1
#     	else:
#     		cache[num] += 1
#     print(cache)
#     for k, v in cache.items():
#     	if k == v:
#     		print (k)
#     print ("-1")


findLucky([1,2,2,3,3,3])

# def frequencySort(nums):
#     cache = {}
#     res = []
#     for num in nums:
#         if num not in cache.keys():
#             cache[num] = 1
#         else:
#             cache[num] += 1

#     new_cache = sorted(cache.items(), key=lambda x: x[1], reverse=True)
#     print(new_cache)
#     for k, v in new_cache:
#         res += ([k] * v)
#     print(res) 





# 1394. Find Lucky Integer in an Array
# Easy

# Given an array of integers arr, a lucky integer is an
# integer which has a frequency in the array equal to its value.

# Return a lucky integer in the array. If there are multiple
# lucky integers return the largest of them.
# If there is no lucky integer return -1.

 

# Example 1:

# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.