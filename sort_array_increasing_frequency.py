class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        res = sorted(nums, key = nums.count)
        return res


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



# def frequencySort(nums):
#     print(nums)
#     #sorts in reverse order ex 3, 2, 1
#     nums.sort(reverse=True)
#     print(nums)
#     #sorts num base on freq (starting from larger ints)
#     res = sorted(nums, key = nums.count)
#     print(res)

# frequencySort([2,3,1,3,2])


# 1636. Sort Array by Increasing Frequency
# Easy

# Given an array of integers nums, sort the array in increasing order based
# on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

 

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:

# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]
 

