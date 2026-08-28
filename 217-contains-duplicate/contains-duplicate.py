class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for x in nums:
            if freq[x] != 1:
                return True

        return False