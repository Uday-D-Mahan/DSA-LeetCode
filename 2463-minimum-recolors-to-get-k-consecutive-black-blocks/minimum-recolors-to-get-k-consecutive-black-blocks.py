class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window_cal = blocks[:k]
        total = window_cal.count("W")
        minimum = total

        for i in range (k , len(blocks)):
           
            if blocks[i-k] == "W":
                total -= 1

            if blocks[i] == "W":
                total += 1

            if total < minimum:
                minimum = total

        return minimum



