class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
       count = {}
       ans = 0
       for i in range (len(nums)):
        if nums[i] in count:
            ans += count[nums[i]]
            count[nums[i]] += 1

        else:
            count[nums[i]] = 1

       return ans
    

        