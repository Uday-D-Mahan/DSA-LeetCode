class Solution:
    def leftRightDifference(self, nums):
        n = len(nums)
        ans = []

        for i in range(n):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            ans.append(abs(left - right))

        return ans
        