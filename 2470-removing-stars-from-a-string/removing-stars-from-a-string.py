class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if not i.isalpha():
                if stack:
                    stack.pop()

            else:
                stack.append(i)

        return "".join(stack)