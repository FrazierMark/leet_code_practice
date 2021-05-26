class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


        # iterater through the array
        # if element == 0,
        # move element to end of array.
        







# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]




# Given an integer array nums,
# move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

#Note that you must do this in-place
# without making a copy of the array.