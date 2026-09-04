class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        add = 0
        mult = 0

        for i in operations:
            if i.lstrip("-").isdigit():
                stack.append(int(i))

            elif i == "C":
                stack.pop()

            elif i == "D":
                mult =stack[-1] * 2
                stack.append(mult)

            else:
                add = stack[-1] + stack[-2]
                stack.append(add)

        return sum(stack)
