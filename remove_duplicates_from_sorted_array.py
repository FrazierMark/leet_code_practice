class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curs = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[curs]:
                curs += 1
                nums[curs] = nums[i]
        return curs + 1





#Given a sorted array nums, remove the duplicates in-place such that
# each element appears only once and returns the new length.

#Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

