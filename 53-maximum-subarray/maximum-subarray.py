class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        largest = float('-inf')
        for i in range (len(nums)):
            curr += nums[i]
            largest = max(largest,curr)
            if curr < 0:
                curr = 0

        return largest 