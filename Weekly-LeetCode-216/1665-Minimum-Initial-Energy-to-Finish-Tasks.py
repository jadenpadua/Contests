# Greedy Hard
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)
        res = cur = 0
        
        for actual, minimum in tasks:
            if minimum > cur:
                res += (minimum-cur)
                cur = minimum 
            cur -= actual
        
        return res
