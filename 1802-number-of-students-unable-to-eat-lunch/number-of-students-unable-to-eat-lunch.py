class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq = {}

        for i in range (len(students)):
            if students[i] not in freq:
                freq[students[i]] = 1

            else:
                freq[students[i]] += 1

        for i in range (len(sandwiches)):
            if sandwiches[i] in freq and freq[sandwiches[i]] > 0:
                freq[sandwiches[i]] -= 1

            else:
                return sum(freq.values())

        return 0

        
