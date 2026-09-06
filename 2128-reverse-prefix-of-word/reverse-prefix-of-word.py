class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack1 = []
        stack2 = []
        result = ""
        ans = 0

        if ch not in word:
            return word

        for i in word:
            stack1.append(i)
            if i == ch:
                break

        for i in word [len(stack1):]:
            stack2.append(i)


        while stack1:
            result += stack1.pop()

        ans = result + "".join(stack2)

        return ans