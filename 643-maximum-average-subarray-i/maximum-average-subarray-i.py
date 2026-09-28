class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maximum = window_sum

        for i in range ( k , len(nums)):

            window_sum = window_sum - nums[i - k] + nums[i]

            if window_sum > maximum:
                maximum = window_sum

        return maximum / k
