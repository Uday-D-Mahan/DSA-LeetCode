class Solution:
    def smallerNumbersThanCurrent(self, nums):
        original = nums[:]

        nums.sort()

        counter = {}
        count = 0

        for x in nums:
            if x not in counter:
                counter[x] = count

            count += 1

        ans = []

        for x in original:
            ans.append(counter[x])

        return ans
            
        
       