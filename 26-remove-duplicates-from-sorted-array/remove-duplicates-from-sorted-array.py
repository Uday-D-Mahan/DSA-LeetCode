class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low = 0
        high = 1
        temp = 1
        while high < len(nums):
            if nums[low] != nums[high]:
                low += 1
                temp += 1
                nums[low] = nums[high]
                
            high += 1
               
        return temp


       