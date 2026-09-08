class Solution:
    def subsetXORSum(self, nums):
        ans = 0

        for num in nums:
            ans |= num

        return ans * (2 ** (len(nums) - 1))
        