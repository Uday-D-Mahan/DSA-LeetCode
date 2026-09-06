class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maximum = 0

        for i in s:
            if i == "(":
                stack.append(i)

                if maximum < len(stack):
                    maximum = len(stack)

            elif i == ")" and ")" != s[0]:
                stack.pop()

        return maximum

        
        
