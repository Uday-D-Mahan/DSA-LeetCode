class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        ans = []
        for i in range (len(nums)):
            if nums[i] in count:
                ans.append(nums[i])
                

            else:
                count[nums[i]] = 1
              

        return ans
        