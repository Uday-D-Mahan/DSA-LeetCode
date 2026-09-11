class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for i in range (len(nums)):
            total = 0
            num = nums[i]

            while num > 0:
                total += num % 10
                num = num // 10

            ans.append(total)

        ans.sort()

        return ans[0]

