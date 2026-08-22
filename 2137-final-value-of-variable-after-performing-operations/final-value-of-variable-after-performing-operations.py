class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ## Uday
        temp = 0
        for i in range (len(operations)):
            if operations[i] == "X++" or operations[i] == "++X":
                temp += 1

            else:
                temp -= 1

        return temp
       