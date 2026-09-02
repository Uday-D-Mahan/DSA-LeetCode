class Solution:
    def moveZeroes(self, nums):
        low = 0
        high = 0

        while high < len(nums):
            if nums[high] != 0:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
            high += 1

        return 0


                
        