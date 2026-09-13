class Solution:
    def findMissingElements(self, nums):
        nums.sort()
        maximum = max(nums)
        stack = []

        x = nums[0]

        while x < maximum:
            if x + 1 in nums:
                x += 1
            else:
                x += 1
                stack.append(x)

        return stack
