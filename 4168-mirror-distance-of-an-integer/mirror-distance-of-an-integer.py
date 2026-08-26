class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        temp = int(str(n)[::-1])
        count = temp - n
        if count < 0:
            count = -(count)

        return count

        
      
       
