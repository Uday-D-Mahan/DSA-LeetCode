from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_element = max(freq.values())
        temp = 0
        for i in range (len(nums)):
            if max_element == freq[nums[i]]:
                temp += 1

        return temp