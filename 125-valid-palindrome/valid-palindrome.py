class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")

        new_s = ""

        for char in s:
             if char.isalnum():
                 new_s += char

        low = 0
        high = len(new_s) - 1


        while low <= high:
            if new_s[low] == new_s[high]:
                low += 1 
                high -= 1
                

            else:
                return False

        return True
