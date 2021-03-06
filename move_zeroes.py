class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


        # iterater through the array
        # if element == 0,
        # move element to end of array.
        



# Smart solution found online- swapping elements

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]




# Given an integer array nums,
# move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

#Note that you must do this in-place
# without making a copy of the array.