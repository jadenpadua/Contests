#Prefix sum Med-Hard
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        
        o_pref, e_pref = [0] * (n+1), [0] * (n+1)
        
        for i, num in enumerate(nums):
            o_pref[i] += o_pref[i-1]
            e_pref[i] += e_pref[i-1]
            
            if i % 2 == 0:
                e_pref[i] += num
            else:
                o_pref[i] += num
        
        result = 0
        for i, num in enumerate(nums):
            e_after_removed = e_pref[i-1] + o_pref[n-1] - o_pref[i]
            o_after_removed = o_pref[i-1] + e_pref[n-1] - e_pref[i]
            result += (e_after_removed == o_after_removed)
        
        return result
