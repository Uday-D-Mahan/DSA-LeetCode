class Solution:
    def removeOuterParentheses(self, s):
        stack = []
        result = []

        for i in s:
            if i == "(":
                if len(stack) > 0:
                    result.append(i)

                stack.append(i)

            else:
                stack.pop()

                if len(stack) > 0:
                    result.append(i)

        return "".join(result)