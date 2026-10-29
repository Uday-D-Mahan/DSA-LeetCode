class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack = []
        low = 0

        for i in range (1 , n + 1):

            if low == len(target):
                break

            stack.append("Push")
            
            if i == target[low]:
                low += 1

            else:
                stack.append("Pop")

        return stack    