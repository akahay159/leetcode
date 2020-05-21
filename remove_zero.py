
Given an array nums,write a function to move all 0's to the end of it while maintaining the relative
order of the non-zero elements
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
   
Solution
=======================================================================================================
class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j = j + 1
        for x in range(j, len(nums)):
            nums[x] = 0
